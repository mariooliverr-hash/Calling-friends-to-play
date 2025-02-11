import pyautogui
import time
import os
import pyperclip

def jogodouser():
    jogo = input("Qual jogo você quer jogar ?")
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write(jogo)
    time.sleep(1)
    pyautogui.press("enter")

def party():
    friendss = input('Qual amigo você quer chamar para a party ?')
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("WhatsApp")
    time.sleep(1)
    pyautogui.press("Enter")
    time.sleep(1)
    pyautogui.click(x=171, y=120)
    time.sleep(1)
    pyperclip.copy(friendss)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)
    pyautogui.click(x=221, y=170)
    time.sleep(1)
    pyautogui.click(x=803, y=827)
    time.sleep(1)
    pyautogui.write("Vamos jogar")
    time.sleep(1)

while True:
    os.system("cls")
    jogodouser()
    party()

    