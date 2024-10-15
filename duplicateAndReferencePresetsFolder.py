import os
from pathlib import Path
from win32com.client import Dispatch

# directory to mirror
ammunition = r"F:\SteamLibrary\steamapps\\common\\projectM\\presets"

# name of new directory
directoryname = "presets_inactive"

# new directory location
targetlocation = r"F:\SteamLibrary\steamapps\\common\\projectM\\" 
target = targetlocation + directoryname

def run():
    createDirectory(target)
    mirrorDirectory(ammunition, directoryname, target, targetlocation)

def mirrorDirectory(startpath, directoryname, targetpath, targetlocation):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        newpath = str(Path(root).resolve()).replace(startpath, targetlocation + chr(92) + directoryname)
        createDirectory(newpath)
        createShortcut(newpath, Path(root).resolve())
        createShortcut(Path(root).resolve(), newpath)

def createDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def createShortcut(path, target):
    print(str(target) + "\\"+ str(os.path.basename(path)) + ".lnk")
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(str(target) + "\\"+ str(os.path.basename(path)) + ".lnk")
    shortcut.Targetpath = str(str(path) )
    shortcut.save()

run() 
print("Finished")