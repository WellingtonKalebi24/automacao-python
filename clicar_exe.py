import pyautogui
import time

def executar_assinador(executor):
    if executor:
        print("🗑️ Aguardando confirmação...")
        print("⏳ Aguardando arquivo baixar...")
        time.sleep(8)
         # confirmar
        pyautogui.click(x=1435, y=610) 
        time.sleep(6)

         # mínimo (ideal: usar verificação de arquivo)

        # assinar com o exe

        pyautogui.hotkey("win", "r")
        pyautogui.write("Downloads")  
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(x=1567, y=289)
        pyautogui.write("assinador")
        time.sleep(0.3)
        pyautogui.doubleClick(x=581, y=376)
        time.sleep(2)
        pyautogui.click(x=1081, y=608)
        time.sleep(1.3)
        pyautogui.click(x=1081, y=608)    