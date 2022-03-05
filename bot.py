from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con
from tkinter import *
import tkinter.messagebox
from tkinter.font import Font
from tkinter import ttk

def start():
    while keyboard.is_pressed('q') == False:
    
        if pyautogui.locateOnScreen('easy.png', confidence=0.8) != None:
            pyautogui.keyDown('down')
            time.sleep(np.random.uniform(0.1,0.15))
            pyautogui.keyUp('down')
            time.sleep(0.5)
            pyautogui.keyDown('\n')
            time.sleep(np.random.uniform(0.1,0.15))
            pyautogui.keyUp('\n')

        elif pyautogui.locateOnScreen('end.png', confidence=0.8)!= None:
            pyautogui.keyDown('\n')
            time.sleep(np.random.uniform(0.1))
            pyautogui.keyUp('\n')
            time.sleep(0.5)
            
        elif pyautogui.locateOnScreen('field.png', confidence=0.8)!= None:
            pyautogui.keyDown('\n')
            time.sleep(np.random.uniform(0.1,0.3))
            pyautogui.keyUp('\n')
            time.sleep(0.5)
            
        elif pyautogui.locateOnScreen('fail.png', confidence=0.8)!= None:
            pyautogui.keyDown('\n')
            time.sleep(np.random.uniform(0.1,0.3))
            pyautogui.keyUp('\n')
            time.sleep(0.5)
            
        elif pyautogui.locateOnScreen('start.png', confidence=0.8)!= None:
            pyautogui.keyDown('\n')
            time.sleep(np.random.uniform(0.03,0.05))
            pyautogui.keyUp('\n')
            time.sleep(np.random.uniform(3.18,3.22))
            pyautogui.keyDown('\n')
            pyautogui.keyUp('\n')

        elif pyautogui.locateOnScreen('playn.png', confidence=0.9) != None:
            pyautogui.keyDown('down')
            time.sleep(np.random.uniform(0.05,0.07))
            pyautogui.keyUp('down')
            time.sleep(np.random.uniform(0.05,0.07))
            pyautogui.keyDown('down')
            time.sleep(np.random.uniform(0.05,0.07))
            pyautogui.keyUp('down')
            time.sleep(np.random.uniform(0.05,0.07))
            pyautogui.keyDown('\n')
            time.sleep(np.random.uniform(0.05,0.07))
            pyautogui.keyUp('\n')
            time.sleep(0.5)
            
        else:
            continue

root = Tk()
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = 'Tucker.png')
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.title('Field Goal Kicker')
root.iconbitmap(r'roboticon.ico')
root.geometry("300x300")
myFont = Font(family="Times New Roman", size=12)
b = Button(root,text="Start",command=start)
b.pack(side='top')
root.mainloop()
