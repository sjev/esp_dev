# test of a stepper motorimport machine


from machine import Pin
import esp
import esp32
from time import sleep, sleep_ms
import time
from uln2003 import Stepper, Driver, Command, FULL_ROTATION, HALF_STEP, FULL_STEP



print('Testing stepper...')

pins = [Pin(p, Pin.OUT) for p in [27,26,25,33]]

def test_pins():
    # flash pins
    for idx in range(4):
        for p in pins:
            p.off()
            p.on()
            sleep(1)
            p.off()

# Full step does not work
stepper = Stepper(HALF_STEP,*pins,delay=1000)

#measure time for a full rotation
t_start = time.ticks_ms()
stepper.step(FULL_ROTATION,1)
delta = time.ticks_diff(time.ticks_ms(),t_start)
print('Revolution time: ',delta)

for idx in range(10):
    stepper.step(FULL_ROTATION,1)
    stepper.step(FULL_ROTATION,-1)

#runner = Driver()

#runner.run([Command(stepper, FULL_ROTATION,1)])
print('Done')
