import pyautogui
import time

time.sleep(30)
txt = open('hewan.txt','r')

for i in txt:
    pyautogui.write("babi kyok "+i)
    pyautogui.press("enter")    

# for i in range(1000):
#     pyautogui.write("test more world")
#     pyautogui.press("enter")
    # pyautogui.press("l")
    # pyautogui.press("o")
    # pyautogui.press("v")
    # pyautogui.press("e")
    # pyautogui.press("enter")
    # pyautogui.press("y")
    # pyautogui.press("o")
    # pyautogui.press("u")
    # pyautogui.press("enter")