import os
from datetime import datetime
import pyperclip
import time
import pyautogui

#get current time
now = datetime.now()
s = str(now)
dt = s[11:-10] + " on " + s[5:-19] + "/" + s[8:-16] + "/" + s[:-22]

print(dt)
path = "/System/Applications/TextEdit.app"
os.system(f"open {path}")
pyperclip.copy(dt)
time.sleep(1)

with pyautogui.hold('command'):
    pyautogui.press(['v'])

pyperclip.copy("SaveFunction")
time.sleep(1)

with pyautogui.hold('command'):
    pyautogui.press(['s'])
time.sleep(1)

with pyautogui.hold('command'):
    pyautogui.press(['v'])
time.sleep(1)

pyautogui.press(['enter'])
