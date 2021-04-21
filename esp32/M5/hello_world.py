from m5stack import lcd
from time import sleep

def reset_lcd():
    lcd.clear()
    lcd.setCursor(0,0)

reset_lcd()
idx = 0
try:
    while True:
        lcd.print('.')
        sleep(0.01)
        idx+=1
        pos = lcd.getCursor()
        if pos[1] > 216:
            reset_lcd()
except:
    lcd.clear()
