#a=left
#d=right
#s=down
#w=up

#i=upleft
#j=upright
#k=downright
#l=downleft

#p= pause

import serial
import pyautogui
port_name="COM"+str(input("COM number :"))
Ard = serial.Serial(port=port_name, baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
Ard.open()
print("type 1 for :-WSAD input")
print("type anything else for :-Arrow input")

mode=int(input('input:'))
while 1:
    read = str(Ard.readline())
    inc = read.decode('ascii')
    print(inc)
#WSAD
    if mode==1:
        if inc=='s':  # if incoming data is 'down'
            pyautogui.press('s')

        elif inc =='w':  # if incoming data is 'up'
            pyautogui.press('w')
    
        elif inc =='a':  # if incoming data is 'left'
            pyautogui.press('a')

        elif inc =='d':  # if incoming data is 'right'
            pyautogui.press('d')

        elif inc =='i':  # if incoming data is 'upleft'
            pyautogui.keyDown('a')
            pyautogui.press('w')
            pyautogui.keyUp('a')

        elif inc =='j':  # if incoming data is 'upright'
            pyautogui.keyDown('d')
            pyautogui.press('w')
            pyautogui.keyUp('d')

        elif inc =='k':  # if incoming data is 'downright'
            pyautogui.keyDown('d')
            pyautogui.press('s')
            pyautogui.keyUp('d')

        elif inc =='l':  # if incoming data is 'downleft'
            pyautogui.keyDown('a')
            pyautogui.press('s')
            pyautogui.keyUp('a')
#Arrow 
    elif mode!=1:
        if inc=='s':  # if incoming data is 'down'
            pyautogui.press('down')

        elif inc =='w':  # if incoming data is 'up'
            pyautogui.press('up')
    
        elif inc =='a':  # if incoming data is 'left'
           pyautogui.press('left')

        elif inc =='d':  # if incoming data is 'right'
            pyautogui.press('right')

        elif inc =='i':  # if incoming data is 'upleft'
            pyautogui.keyDown('left')
            pyautogui.press('up')
            pyautogui.keyUp('left')

        elif inc =='j':  # if incoming data is 'upright'
            pyautogui.keyDown('right')
            pyautogui.press('up')
            pyautogui.keyUp('right')

        elif inc =='k':  # if incoming data is 'downright'
            pyautogui.keyDown('right')
            pyautogui.press('down')
            pyautogui.keyUp('right')

        elif inc =='l':  # if incoming data is 'downleft'
            pyautogui.keyDown('left')
            pyautogui.press('down')
            pyautogui.keyUp('left')
    read = "";    
    inc = "";  # clears the data
