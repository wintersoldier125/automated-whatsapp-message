import pyautogui
import time

time.sleep(5)
count = 0

while count<5:
    pyautogui.typewrite("hello")
    pyautogui.press("enter")
    count +=1