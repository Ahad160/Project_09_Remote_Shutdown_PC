import pyautogui
import subprocess
import time

subprocess.Popen(['start', 'cmd'], shell=True)

time.sleep(2)

pyautogui.typewrite("shutdown /i")
pyautogui.press("enter")

time.sleep(4)

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

pyautogui.typewrite("192.168.0.108") #🔴 Enter Youer Target PC IP Address
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

pyautogui.press("tab")
pyautogui.press("tab")
time.sleep(1)
pyautogui.press("s")

for i in range(0, 5):
    pyautogui.press("tab")


time.sleep(1)
pyautogui.typewrite("PC Will Shutdown Within 30 Secend")
pyautogui.press("tab")
pyautogui.press("enter")


time.sleep(30)
pyautogui.typewrite("cls")
pyautogui.press("enter")
pyautogui.typewrite("exit")
pyautogui.press("enter")






















