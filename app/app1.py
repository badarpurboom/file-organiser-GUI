import eel
import tkinter  as tk
from tkinter import filedialog
import os
import glob


eel.init('web')

@eel.expose
def op():
    root=tk.Tk()
    root.withdraw()
    path=filedialog.askdirectory()
    os.chdir(path)

    files_list = glob.glob("*")
    extension_set = set()

    for file in files_list:
        extension = file.split(sep=".")
        try:
            extension_set.add(extension[1])
        except IndexError:
            continue


    def createDirs():
        for dir in extension_set:
            try:
                os.makedirs(dir+"_files")
            except FileExistsError:
                continue

    def arrange():
        for file in files_list:
            fextension = file.split(sep=".")
            try:
                os.rename(file, fextension[1]+"_files/"+file)
            except (OSError, IndexError):
                continue

@eel.expose
def start():
    
    files_list = glob.glob("*")
    extension_set = set()

    for file in files_list:
        extension = file.split(sep=".")
        try:
            extension_set.add(extension[1])
        except IndexError:
            continue


    def createDirs():
        for dir in extension_set:
            try:
                os.makedirs(dir+"_files")
            except FileExistsError:
                continue

    def arrange():
        for file in files_list:
            fextension = file.split(sep=".")
            try:
                os.rename(file, fextension[1]+"_files/"+file)
            except (OSError, IndexError):
                continue
    createDirs()
    arrange()


eel.start("home.html", size=(300, 400))
