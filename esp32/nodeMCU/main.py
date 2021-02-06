import machine
from machine import Pin
import esp
import esp32
from time import sleep, sleep_ms

led = Pin(2, Pin.OUT)
led.off()

print('Welcome to NodeMCU')



for idx in range(5):
    led.on()
    sleep_ms(100)
    led.off()
    sleep_ms(100)
