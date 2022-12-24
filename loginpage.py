from tkinter import *
from functools import partial
d={}
def login(username,password):
    global d;
    print("username is",username.get())
    print("password is",password.get())
    
    d["name"]=username.get()
    d["pass"]=password.get()
    print(d)
    return
tkwindow=Tk()
tkwindow.geometry('600x150')
tkwindow.title("login page")
usernamelabel=Label(tkwindow,text="Username").grid(row=0,column=0)
username=StringVar()
unsernameEntry=Entry(tkwindow,textvariable=username).grid(row=0,column=1)
passwordLabel=Label(tkwindow,text="Password").grid(row=1,column=0)
password=StringVar()
passwordEntry=Entry(tkwindow,textvariable=password,show='*').grid(row=1,column=1)
login=partial(login,username,password)
loginButton=Button(tkwindow,text='Login',command=login).grid(row=4,column=3)
tkwindow.mainloop()
