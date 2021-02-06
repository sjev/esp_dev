import machine
from machine import Pin
import esp
import esp32
from time import sleep

esp.osdebug(None)       # turn off vendor O/S debugging messages
esp.osdebug(0)          # redirect vendor O/S debugging messages to UART(0)


print('Welcome to ESP32')
print('Flash size ', esp.flash_size())

for idx in range(10):
    print('hall:',esp32.hall_sensor())
    sleep(1)
