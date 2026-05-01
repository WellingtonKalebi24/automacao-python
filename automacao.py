import pyautogui
import time

pyautogui.PAUSE = 0.3 # a cada comando demora 3 milisegundos

# pegar position do mouse e da tela
print(pyautogui.position())
print(pyautogui.size())


# funcoes do mouse  
time.sleep(5)

pyautogui.click(x=-591, y=332) # clica em algum lugar
time.sleep(2)
pyautogui.click(x=-612, y=654)

# pyautogui.moveTo(x=-591, y=332, duration=0.5) mover mouse
# pyautogui.scroll(1000) dar um scroll na tela

# funcoes de teclado
# pyautogui.write("Ola mundo")
# pyautogui.hotkey("ctrl", "c")
# pyautogui.hotkey("ctrl", "v")
# pyautogui.press("enter")