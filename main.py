import pyautogui
import time
import os
import pyperclip

def gameuser():
    game = input("Which game do you want to play?")
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write(game) #Write the name of the game the user is going to play.
    time.sleep(1)
    pyautogui.press("enter") 

def party():
    friends = input('Which friend do you want to invite to the party?')
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("WhatsApp") #Open WhatsApp.
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=171, y=120)
    time.sleep(1)
    pyperclip.copy(friends) #Copy the friend's name from the user.
    pyautogui.hotkey("ctrl", "v") #Paste the friend's name that the user wants to invite to the party.
    time.sleep(1)
    pyautogui.click(x=221, y=170)
    time.sleep(1)
    pyautogui.click(x=803, y=827)
    time.sleep(1)
    pyautogui.write("Let's play") #Send the message inviting the friend to the party.
    time.sleep(1)
    pyautogui.press("enter") #Send the message.
while True: 
    os.system("cls") #Loop running so that the previous commands are erased.
    gameuser()
    party()