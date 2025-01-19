import pyfirmata2

comport='COM5'

board=pyfirmata2.Arduino(comport)


led_1=board.get_pin('d:3:o')

def led(fingerUp):
    if fingerUp==[0,1,0,0,0]:
        led_1.write(1)
    else:
        led_1.write(0)
