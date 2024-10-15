import os
from pathlib import Path
from win32com.client import Dispatch

# !!replace every \ with chr(92)
# or dont touch them if they work

# directory to mirror
ammunition = r"F:\SteamLibrary\steamapps" + chr(92) + "common" + chr(92) + "projectM" + chr(92) + "presets"

# name of new directory
directoryname = "presets_inactive"

# new directory location
targetlocation = r"F:\SteamLibrary\steamapps" + chr(92) + "common" + chr(92) + "projectM"
target = targetlocation + directoryname

def run():
    createDirectory(target)
    mirrorDirectory(ammunition, directoryname, target, targetlocation)

def mirrorDirectory(startpath, directoryname, targetpath, targetlocation):
    for root, dirs, files in os.walk(startpath):
        newpath = str(Path(root).resolve()).replace(r"\projectM\presets", r"\projectM" + chr(92) + directoryname)
        createDirectory(newpath)
        createShortcut(newpath,              Path(root).resolve())
        createShortcut(Path(root).resolve(), newpath             )

def createDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def createShortcut(path, target):
    filename = str(target) + chr(92) + str(os.path.basename(path)) + ".lnk"
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(filename)
    shortcut.Targetpath = str(str(path) )
    shortcut.save()
    print(filename)

run() 
print("Finished")