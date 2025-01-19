import pyfirmata2

comport='COM5'

board=pyfirmata2.Arduino(comport)


led_1=board.get_pin('d:3:o')

import time

last_detected = None  # 마지막으로 'dog'가 탐지된 시간

def led(cls):
    global last_detected
    
    if cls == 'dog':
        # 'dog'가 탐지되면 LED를 켠다.
        led_1.write(1)
        last_detected = time.time()  # 'dog'가 탐지된 시간을 기록
    elif last_detected is not None:
        # 'dog'가 더 이상 탐지되지 않으면, 마지막으로 탐지된 시간이 10초 이상 경과하면 LED를 끈다.
        if time.time() - last_detected > 1:
            led_1.write(0)  # 10초 경과 후 LED 끄기
            last_detected = None  # 타이머 초기화
        else:
            # 'dog'가 탐지되지 않은 경우 계속 켜두기
            led_1.write(1)
