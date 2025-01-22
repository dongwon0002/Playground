import sqlite3
import datetime
import os

class DatabaseHandler:
    def __init__(self, db_name="detections.db"):
        self.db_name = os.path.join(os.getcwd(), db_name)
        self.initialize_db()

    def initialize_db(self):
        """데이터베이스 초기화 (테이블 생성)"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        #생성 db 데이터 명, 형식 입력력
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS detections (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                class_name TEXT,
                confidence REAL,
                count INT,
                x1 INT,
                y1 INT,
                x2 INT,
                y2 INT       
            )
        ''')
        conn.commit()
        conn.close()

    def save_detection(self, class_name, confidence, count, x1, y1, x2, y2):
        """감지된 데이터를 데이터베이스에 저장"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # db에 데이터 입력 qeury 작성 
        # execute("INSERT INTO (db이름) (컬럼) VALUES (미지정_데이터)", (입력할_데이터))
        cursor.execute('''
            INSERT INTO detections (timestamp, class_name, confidence, count, x1, y1, x2, y2)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (timestamp, class_name, confidence, count, x1, y1, x2, y2))
        #db commit하고 닫아야 된다
        conn.commit()
        conn.close()

