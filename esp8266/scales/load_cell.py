# scales test


from machine import Pin

from time import sleep, sleep_ms
import time
from hx711 import HX711

from machine import freq
freq(160000000)

# connections
SCK = 14
DT = 16

print('Testing load cell')
driver = HX711(d_out=DT, pd_sck=SCK)

while True:
    val = driver.read()
    print(val)
