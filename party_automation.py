import pyautogui
import time
import os
import pyperclip
import speech_recognition as sr

def jogo_usuario(texto):
    print("Qual jogo você quer jogar?")
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write(texto)  # Escreve o nome do jogo que o usuário vai jogar.
    time.sleep(1)
    pyautogui.press("enter")

def festa():
    amigo = input('Qual amigo você quer convidar para a festa? ')
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("WhatsApp")  # Abre o WhatsApp.
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=171, y=120)
    time.sleep(1)
    pyperclip.copy(amigo)  # Copia o nome do amigo informado pelo usuário.
    pyautogui.hotkey("ctrl", "v")  # Cola o nome do amigo que o usuário quer convidar.
    time.sleep(1)
    pyautogui.click(x=221, y=170)
    time.sleep(1)
    pyautogui.click(x=803, y=827)
    time.sleep(1)
    pyautogui.write("Vamos jogar")  # Envia a mensagem convidando o amigo para a festa.
    time.sleep(1)
    pyautogui.press("enter")  # Envia a mensagem.

def voz():
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as fonte:
        print("Diga algo...")
        audio = reconhecedor.listen(fonte)
    try:
        texto = reconhecedor.recognize_google(audio, language="pt-br")
        jogo_usuario(texto)
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
    except sr.RequestError as e:
        print(f"Erro ao acessar o serviço: {e}")

while True:
    os.system("cls")  # O loop roda para apagar os comandos anteriores.
    voz()
   
