import subprocess
import win32api
import win32gui
import time
import win32con
import psutil
import pyautogui

hwnd = win32gui.FindWindow(None, "Advertisement")
print(hwnd)
title = win32gui.GetWindowText(hwnd)
print(title)
script2 = "window.py"
            
def main2():
    global check
    ad = True
    while ad:
        global current
        current = win32gui.GetForegroundWindow()
        hwnd = win32gui.FindWindow(None, "Advertisement")
        title = win32gui.GetWindowText(hwnd)
        if title == "Advertisement":
            time.sleep(1)
            subprocess.Popen("taskkill /im Spotify.exe /f")
            time.sleep(0.5)
            subprocess.Popen("Spotify.exe") 
            time.sleep(1)
            pyautogui.hotkey("ctrl", "right")
            time.sleep(1)
            ad = False
            check = True 
        else:    
            ad = False 
 



def is_app_running(app_name):
    for process in psutil.process_iter(['pid', 'name']):
        if app_name.lower() in process.info['name'].lower():
            return True



#main program
app_name_to_check = "Spotify.exe"  
check = True
while check:
    if is_app_running(app_name_to_check):
        main2()

    else:
        print(f"App {app_name_to_check} is not running.")

