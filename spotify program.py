import subprocess
import win32api
import win32gui
import time
import win32con
import psutil
import pyautogui


#tož fachá to když to hraje i když se to přepne, jenže jakmile se to znova zapne tak se aktivní okno zmenší (jenom když program zapnu po spotify) a ten space se dá v tom okně


hwnd = win32gui.FindWindow(None, "Advertisement")
print(hwnd)
title = win32gui.GetWindowText(hwnd)
print(title)
script2 = "window.py"


#def get_window():
#    print("mam okno")
#    return win32gui.GetForegroundWindow()
#    
#
#def focus_on(spotify_window):
#    print("focus")
#    #win32gui.ShowWindow(handle, win32con.SW_RESTORE)
#    win32gui.SetForegroundWindow(spotify_window)
# 
#    
#def press_key(key):
#    print("press")
#    pyautogui.press(key) 


#def main():
#    ad = True
#    while ad:
#        hwnd = win32gui.FindWindow(None, "Slipknot - Nero Forte")
#        print(hwnd)
#        title = win32gui.GetWindowText(hwnd)
#        print(title)
#        if title == "Slipknot - Nero Forte":
#            prev_window = get_window()
#            subprocess.Popen("taskkill /im Spotify.exe /f")
#            time.sleep(0.5)
#            print("kok")
#            #return True
#            print("close")
#            subprocess.Popen("Spotify.exe")
#            print("open")
#            spotify_window = win32gui.FindWindow(None, "Spotify")
#            focus_on(spotify_window)
#            press_key("Space")
#            time.sleep(0.5)
#            print("space je done")
#            focus_on(prev_window) 
#            print("focus na "+str(prev_window) )   
#            ad = False  
#        else: 
#            
#            ad = False
#            #return False  
            

#def focus_and_click():
#    #global current
#    #current = win32gui.GetForegroundWindow()
#    spotify = win32gui.FindWindow(None, "Spotify Free")
#    win32gui.SetForegroundWindow(spotify)
#    pyautogui.press("space")
#    prev_focus()
    
#def prev_focus():    
#    win32gui.SetForegroundWindow(current)
    
#def easy():
#    spotify = win32gui.FindWindow(None, "Spotify Free")
#    WM_KEYDOWN = 0x0100
#    WM_KEYUP = 0x0101
#    VK_SPACE = 0x20
#    win32gui.PostMessage(spotify, WM_KEYDOWN, VK_SPACE, 0)
#    win32gui.PostMessage(spotify, WM_KEYUP, VK_SPACE, 0)
    
#def easy2():
#    win32gui.SetActiveWindow()
#    pyautogui.press("space") 
#    win32gui.SetForegroundWindow(current)
#    print("done") 
            
def main2():
    global check
    ad = True
    while ad:
        global current
        current = win32gui.GetForegroundWindow()
        hwnd = win32gui.FindWindow(None, "Advertisement")
        print(hwnd)
        title = win32gui.GetWindowText(hwnd)
        print(title)
        if title == "Advertisement":
            time.sleep(1)
            subprocess.Popen("taskkill /im Spotify.exe /f")
            time.sleep(0.5)
            print("kok")
            #return True
            print("close")
            subprocess.Popen("Spotify.exe") 
            print("open")
            time.sleep(1)
            #focus_and_click()
            #easy()
            #spotify = win32gui.FindWindow(None, "Spotify Free")
            #win32gui.SetForegroundWindow(spotify)
            #pyautogui.press("space")
            pyautogui.hotkey("ctrl", "right")
            #win32gui.SetForegroundWindow(current)
            #prev_focus()
            time.sleep(1)
            ad = False
            check = True 
            print("check done")
        else: 
            
            ad = False
            #return False  
 



def is_app_running(app_name):
    for process in psutil.process_iter(['pid', 'name']):
        if app_name.lower() in process.info['name'].lower():
            return True
    #return False


#main program
app_name_to_check = "Spotify.exe"  
check = True
while check:
    if is_app_running(app_name_to_check):
        #print(f"App {app_name_to_check} is running.")
        main2()
        #if main() == True:
            #subprocess.Popen("Spotify.exe")
            #print("run")
        #else: pass

    else:
        print(f"App {app_name_to_check} is not running.")
        #check = False
    
    
#while is_app_running(app_name_to_check):
 #   main()


#subprocess.Popen("Spotify.exe")
#win32api.SetCursorPos((50,90))

#subprocess.Popen('taskkill /im notepad.exe /f')
#Advertisement

