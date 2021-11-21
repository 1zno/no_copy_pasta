import pyautogui
import time

time.sleep(5)
s = open('file name here', 'r')

lst = [x.lstrip() for x in s]

for x in lst:
    pyautogui.typewrite(x + "\n")
