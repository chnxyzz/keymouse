import key
import time
import scancode

time.sleep(1)
sleeptime=0.5

s='asdfqwer'
while 1:
    key.key_press(0x0f)
    time.sleep(sleeptime)
    for i in s:
        key.key_press(scancode.sc['i'])
        time.sleep(sleeptime)