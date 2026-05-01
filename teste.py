import pyautogui
import time



pyautogui.PAUSE = 0.3 # a cada comando demora 3 milisegundos


pyautogui.press("win")
pyautogui.write("chrome")

time.sleep(2)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=767, y=565)

pyautogui.write("https://www.esocial.gov.br/portal/")
pyautogui.press("enter")

time.sleep(3)
pyautogui.click(x=1000, y=400)
