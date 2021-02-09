import time
import pyautogui

# Give some time before it runs this file
time.sleep(5)

# Finding Mouse's current position on the screen
# print(pyautogui.position())

# the instagram is located at x=470, y=586
pyautogui.moveTo(470, 586)
# pyautogui.scroll(-1200)
for i in range(5):
    time.sleep(3)
    pyautogui.doubleClick()
    time.sleep(3)
    pyautogui.scroll(-1200)

