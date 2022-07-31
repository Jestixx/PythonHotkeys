import keyboard
import time as t

while True: 
    if keyboard.read_key() =="":
       keyboard.press_and_release("") 
       t.sleep(0.1)
