import pyfirmata2
## csv를 사용하는 경우우
# from save_csv import DetectionLogger
from sql_db import DatabaseHandler
comport='COM5'

logger = DatabaseHandler()
logger.initialize_db()
board=pyfirmata2.Arduino(comport)


led_1=board.get_pin('d:3:o')

import time

last_detected = None  # 마지막으로 'dog'가 탐지된 시간
counts = 0
start_time = time.time()

def led(cls, confidence, x1, y1, x2, y2):
    global last_detected
    global counts
    global start_time

    current_time = time.time()

    if current_time - start_time > 1:
        counts = 0
        start_time = current_time

    if cls == 'dog':
        counts += 1  
        last_detected = current_time
        led_1.write(1)  # LED 켜기
        logger.save_detection(cls, confidence, counts, x1, y1, x2, y2)  # count는 1로 저장 (1초동안 유지)

    elif last_detected is not None:
        # 'dog'가 탐지된 후 1초가 지나면 LED를 끄기
        if current_time - last_detected > 1:
            led_1.write(0)  # LED 끄기
            last_detected = None  # last_detected 초기화
        else:
            led_1.write(1)