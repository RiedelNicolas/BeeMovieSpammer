import pyautogui, time
stream = open("script.txt","r")

time.sleep(10)

for word in stream:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
