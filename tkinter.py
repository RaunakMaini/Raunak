from tkinter import *
t=Tk()
def add():
    messagebox.showinfo("info","click on button")
t.geometry("400x400")
name=Label(t,text="enter the first number").place(x=30,y=50)
b=Button(t,text="register",command=add,activeforeground="red",bg="pink")
b.place(x=100,y=200)
t.mainloop()
