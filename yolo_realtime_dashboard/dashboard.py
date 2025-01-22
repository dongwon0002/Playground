import streamlit as st
import sqlite3
import time
import pandas as pd
import plotly.express as px
import altair as alt


####
db_path = ##db.path
#####


# #cache비활성화 가능
# # show_spinner=False : 로딩중임을 표시하는 스피너를 비활성화
# # persist=False : 애플리케이션 재시작 하거나 캐시가 애플리케이션을 종료하면 사라지고 매번 새로 로드드
# @st.cache_data(ttl=0, show_spinner=False, persist=False)
# 최신 500개 탐지 데이터 가져오기 함수
def get_latest_detection():
    """가장 최근의 탐지 데이터를 가져옴"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, timestamp, class_name, confidence, count, x1, y1, x2, y2 
        FROM detections
        ORDER BY id DESC
        LIMIT 500
    ''')
    result = cursor.fetchall()
    conn.close()

    if result:
        columns = ["id", "timestamp", "class_name", "confidence", "count", "x1", "y1", "x2", "y2"]
        df = pd.DataFrame(result, columns=columns)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['minute'] = df['timestamp'].dt.minute
        return df
    else:
        return None

st.set_page_config(page_title="Real-time Object Detection Dashboard", layout="wide")

# 대시보드 제목
st.title("Real-time Object Detection Dashboard")

# 동적으로 업데이트할 공간을 생성

df = get_latest_detection()

class_filter = st.selectbox("Select the Class", pd.unique(df["class_name"]))

detection_display = st.empty()

# 1초마다 새로고침하고 실시간 데이터 갱신

with detection_display.container():
    i = int(time.time())
    df = get_latest_detection()

    if df is not None:
        df_grouped = df.groupby(['timestamp', 'minute', 'class_name'], as_index=False)['count'].max()
        df_minute = df_grouped.groupby(['minute', 'class_name'], as_index=False)['count'].sum()
        df = df[df["class_name"]==class_filter]

    with detection_display.container():
        col1, col2, col3 = st.columns([2,1,1])
        if not df.empty:
            col1.metric(label = "Timestamp",value = str(df.iloc[0]['timestamp']))
            col2.metric(label = "Class",value = (df.iloc[0]['class_name']))
            col3.metric(label = "Count",
                        value = int(df.iloc[0]['count']),
                        delta = int(df_grouped.iloc[0]['count']-df_grouped.iloc[1]['count']))
        else:
            col1.write("No data available")

        fig1, fig3 = st.columns(2)


        with fig1:
            st.markdown("### count change - Plotly")
            fig = px.line(df_grouped, x='timestamp', y='count')
            st.plotly_chart(fig, key=f"plotly-{i}", use_container_width=True)
        with fig3:
            st.markdown("### Count Change - Altair")
            chart = alt.Chart(df_grouped).mark_line().encode(
                x = alt.X(
                    'timestamp:T',
                    axis=alt.Axis(format='%H:%M:%S',
                                  labelAngle=-45)
                ),
                y='count:Q'
            ).properties(title="Count Change (Altair)")
            st.altair_chart(chart, key=f"altair-{i}")

        st.markdown("### Count Change - Bar Chart with Rounded Edges")
        fig = px.bar(df_minute, 
                     x='minute', 
                     y='count', 
                     color='class_name',  # class_name별로 색상 다르게 설정
                     title="Class-wise Count Sum by Minute",
                     labels={'minute': 'Minute', 'count': 'Sum of Count'},
                     color_discrete_sequence=px.colors.qualitative.Set1)  # 색상 설정

        # Bar chart의 각 막대에 라운드 처리
        fig.update_traces(marker=dict(line=dict(width=0, color='black'), 
                                      cornerradius=5))  # Rounded edges 설정
        st.plotly_chart(fig, use_container_width=True)

        # 데이터 프레임 상위 5개 표시시
        st.markdown("### Data Table")
        st.dataframe(df.head())
        


time.sleep(1)
st.rerun()

