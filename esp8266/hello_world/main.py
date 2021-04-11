
from machine import Pin, Signal
from time import sleep


def main():

    led_pin = Pin(2, Pin.OUT)
    led = Signal(led_pin, invert=True)

    idx = 0
    while True:
        print('hello there! # %i' % idx)
        led.value(not led.value())
        idx += 1
        sleep(1)


print('starting main')
main()
