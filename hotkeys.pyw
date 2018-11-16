# link for powershell
#https://www.powershellmagazine.com/2014/04/18/automatic-remote-desktop-connection/
 
# link to python hotkey tutorial
#https://www.youtube.com/watch?v=n_dfv5DLCGI
 
# startup silently
# https://stackoverflow.com/questions/31130960/run-a-program-at-start-up-on-python-in-windows
 
# find startup folder
# window+r, shell:startup
 
from pynput import keyboard
import subprocess
import time
import os
 
jupyter_COMBINATIONS = [
  {keyboard.Key.shift, keyboard.KeyCode(char = 'j'), keyboard.KeyCode(char = 'n')},
  {keyboard.Key.shift, keyboard.KeyCode(char = 'J'), keyboard.KeyCode(char = 'n')},
  {keyboard.Key.shift, keyboard.KeyCode(char = 'j'), keyboard.KeyCode(char = 'N')},
  {keyboard.Key.shift, keyboard.KeyCode(char = 'J'), keyboard.KeyCode(char = 'N')},
  ]

jupyter_lab_COMBINATIONS = [
  {keyboard.Key.shift, keyboard.KeyCode(char = 'j'), keyboard.KeyCode(char = 'l')},
  {keyboard.Key.shift, keyboard.KeyCode(char = 'J'), keyboard.KeyCode(char = 'l')},
  {keyboard.Key.shift, keyboard.KeyCode(char = 'j'), keyboard.KeyCode(char = 'L')},
  {keyboard.Key.shift, keyboard.KeyCode(char = 'J'), keyboard.KeyCode(char = 'L')},
  ]
 
google_news_COMBINATIONS = [
  {keyboard.Key.shift, keyboard.KeyCode(char = 'g'), keyboard.KeyCode(char = 'o')},
  {keyboard.Key.shift, keyboard.KeyCode(char = 'G'), keyboard.KeyCode(char = 'o')},
  {keyboard.Key.shift, keyboard.KeyCode(char = 'g'), keyboard.KeyCode(char = 'O')},
  {keyboard.Key.shift, keyboard.KeyCode(char = 'G'), keyboard.KeyCode(char = 'O')},
  ]
 
#activate.bat calls conda prompt
#C:\Users\xxx\AppData\Local\Continuum\anaconda3\Scripts
def start_jupyter():
    time.sleep(1)
    subprocess.Popen(["C:\\Users\\xxx\\Documents\\Python Scripts\\python-hotkeys.pyw"], shell=True)
    os.system("activate.bat & jupyter notebook")
    os._exit(0)
                
def start_jupyter_lab():
    time.sleep(1)
    subprocess.Popen(["C:\\Users\\xxx\\Documents\\Python Scripts\\python-hotkeys.pyw"], shell=True)
    os.system("activate.bat & jupyter lab")
    os._exit(0)
 
def start_google_news():
    os.system('start chrome "https://news.google.com/?hl=en-US&gl=US&ceid=US:en"')       
                
def on_press(key):
    current.add(key)
    if any(current == combo for combo in jupyter_lab_COMBINATIONS):
        start_jupyter_lab()
        return False
    elif any(current == combo for combo in jupyter_COMBINATIONS):
        start_jupyter()
        return False
    elif any(current == combo for combo in google_news_COMBINATIONS):
        start_google_news()
        return False
 
def on_release(key):
    if key in current:
        current.remove(key)
 
while True:
    current = set()
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()
    time.sleep(2)