import pyautogui
import time
msg = input("Enter the message: ")
n = input("How many times ?: ")
# time.sleep(3000)
for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')
  pyautogui.press("enter")