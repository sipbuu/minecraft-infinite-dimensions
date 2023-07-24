import os
import logging, sys
import time
import sched
from typing import Text
#TEST
from time import sleep
#WAIT
import ctypes
EnumWindows = ctypes.windll.user32.EnumWindows
GetWindowThreadProcessId = ctypes.windll.user32.GetWindowThreadProcessId
EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible
IsWindowEnabled = ctypes.windll.user32.IsWindowEnabled
import win32gui #from win32
import win32api #from win32
import win32console #from win32
from pythonwin import win32ui
import win32con
import string
import random

from time import sleep
#just import EVERYTHING DONT CARE

window_name = "C:\Windows\system32\cmd.exe" #name of the window in use
win32console.SetConsoleTitle("random dimension every few seconds by: besteres, modified by: sipbuu") 
def main():
    print("---CREDITS ----------")
    print("made by besteres, modified by sipbuu [more info abt it at github.]")
    print("--------------------")
    print(" ")
    print("---IMPORTANT INFO --------------")
    print(" ")
    print("make sure that your SERVER command prompt is named 'C:\Windows\system32\cmd.exe'! or else it will not work with this, for info on how to even set up a server/get a hosting service, search up tutorials online.")
    print("and remember to not minimize this application or the command prompt... Have fun!")
    print("---------- ")
    print(" ")
    sleep(1.3)
    print("Type any integer number to be used as the time before each loop. (in seconds)")
    input_interval = input()
    try: #verify if input_interval is an integer
        interval = int(input_interval)

    except ValueError: #this happens if theres an error (input was not an integer)
        print("not an integer, using basic value: 60 seconds now.")
        interval = 60
    sleep(2.5)
    print(" ")
    print("Prepare, you will be teleported in", interval, "seconds.")
    print("If any errors occur or the script doesnt work, restart the file, and check the important info.")
    print(" ")
    thwnd = win32gui.FindWindow(None, window_name) 
    twin = win32ui.CreateWindowFromHandle(thwnd)

    finishRest(twin, thwnd)

    sleep(interval)
    Send_Commands(interval)  


def definedimension(win_):
    maxlenght = random.randint(5, 9) 
    code = [None] * maxlenght 
    for x in range(maxlenght):
        random_crap = ''.join(random.choice(string.ascii_uppercase) for _ in range(1)) 
        code[x] = random_crap 
        win_.SendMessage(win32con.WM_CHAR, ord(random_crap), 0) 
    print("Dimension code is: ", *code, sep='') 


def finishRest(win, hwnd):
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('x'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('c'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('t'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('r'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('n'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('f'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('n'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('c'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('t'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('i'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('o'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('n'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('t'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('i'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('m'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('r'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('b'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('r'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(':'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('r'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('n'), 0)
    sleep(1)
    win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    sleep(1)
    win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
def playerSpawn(win, hwnd):
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('x'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('c'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('t'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('t'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('@'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('p'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('r'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('n'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('s'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('p'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('w'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('n'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('p'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('o'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('i'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('n'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('t'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('@'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    sleep(1)
    win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    sleep(1)
    win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
def Send_Commands(inter_):
    
    timeleft = inter_
    hwnd = win32gui.FindWindow(None, window_name) 
    win = win32ui.CreateWindowFromHandle(hwnd) 

    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('x'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('c'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('t'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('e'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('s'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('@'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('r'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('u'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('n'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0)
    win.SendMessage(win32con.WM_CHAR, ord('w'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('a'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('r'), 0)
    win.SendMessage(win32con.WM_CHAR, ord('p'), 0)
    win.SendMessage(win32con.WM_CHAR, ord(' '), 0) 
    definedimension(win) 
    sleep(1)
    win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    sleep(1)
    win.PostMessage(win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    
    sleep(1)

    finishRest(win, hwnd) #datapack finishes the rest
    sleep(1)

    playerSpawn(win, hwnd) #in case player is not using datapack
    sleep(1)

    print("Teleported, and set the spawn.")
    sleep(timeleft)
    Send_Commands(timeleft)

main() 



