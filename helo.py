from Tkinter import *
import Tkinter as tk
import RPi.GPIO as GPIO
import time
import tkFont
from threading import Thread

    
win=Tk()
win.title('check')
win.geometry('800x480')

mybutton1=Button(win,bg='gray',text='move forward')
mybutton2=Button(win,bg='gray',text='move backward')


mybutton1.pack(pady=20)
mybutton2.pack(pady=20)

def funti():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(15, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(14, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    GPIO.setwarnings(False)
    while 1:
        if GPIO.input(15)==GPIO.HIGH:
            mybutton1.configure(bg='red')
            tk.Label(win, text='move forward',fg = "blue",bg = "yellow",font = "Verdana 10 bold").pack()
            time.sleep(0.2)
            
        else:
            print('not press')
            mybutton1.configure(bg='gray')
            
            
        if GPIO.input(14)==GPIO.HIGH:
            mybutton2.configure(bg='blue')
            tk.Label(win, text="Move Backward",fg = "black",bg = "white",font = "Verdana 10 bold").pack()
            time.sleep(0.2)
            
        else:
            mybutton2.configure(bg='gray')
           
            
    
t1=Thread(target=funti)    
t1.start()
win.mainloop()