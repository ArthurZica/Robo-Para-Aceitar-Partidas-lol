import pyautogui
import time


buscando = "sim"

while buscando == "sim":
    try:
        localizacao = pyautogui.locateCenterOnScreen("Botao.png", confidence=0.5)
        pyautogui.click(localizacao.x, localizacao.y) 
        buscando = "não"
    except:
        time.sleep(1)
        print("não encontrei")
