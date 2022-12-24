from tkinter import*
from tkinter import messagebox
from functools import partial
t=Tk()
t.geometry("400x400")
m=Menubutton(t,text="File",relief=FLAT)
m.pack()
m.menu=Menu(m)
m["menu"]=m.menu
m.menu.add_checkbutton(label="New File")

m.menu.add_checkbutton(label="Open File")

m.menu.add_checkbutton(label="Open Folder")
