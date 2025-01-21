import streamlit as st
import sqlite3
import time
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt


# 최신 30개 탐지 데이터 가져오기 함수
def get_latest_detection():
    """가장 최근의 탐지 데이터를 가져옴"""
    conn = sqlite3.connect('detections.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, timestamp, class_name, confidence, count, x1, y1, x2, y2 
        FROM detections
        ORDER BY id DESC
        LIMIT 30
    ''')
    result = cursor.fetchall()
    conn.close()

    if result:
        columns = ["id", "timestamp", "class_name", "confidence", "count", "x1", "y1", "x2", "y2"]
        df = pd.DataFrame(result, columns=columns)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
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
        df = df[df["class_name"]==class_filter]
        df_grouped = df.groupby('timestamp', as_index=False)['count'].max()

    with detection_display.container():
        col1, col2, col3 = st.columns([2,1,1])
        if not df.empty:
            col1.metric(label = "Timestamp",value = str(df.iloc[0]['timestamp']))
            col2.metric(label = "Class",value = (df.iloc[0]['class_name']))
            col3.metric(label = "Count",
                        value = int(df.iloc[0]['count']),
                        delta = int(df.iloc[0]['count']-df.iloc[1]['count']))
        else:
            col1.write("No data available")

        fig1, fig3 = st.columns(2)


        with fig1:
            st.markdown("### count change - Plotly")
            fig = px.bar(df_grouped, x='timestamp', y='count')
            st.plotly_chart(fig, key=f"plotly-{i}", use_container_width=True)
        with fig3:
            st.markdown("### Count Change - Altair")
            chart = alt.Chart(df_grouped).mark_bar().encode(
                x='timestamp:T',
                y='count:Q'
            ).properties(title="Count Change (Altair)")
            st.altair_chart(chart, key=f"altair-{i}")

        st.markdown("### Data Table")
        st.dataframe(df)
        


time.sleep(1)
st.rerun()

