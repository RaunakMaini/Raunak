from tkinter import*
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id=e_id.get()
    name=e_name.get()
    number=e_number.get()
    email=e_email.get()
    if(id=="" or name=="" or number=="" or email==""):
        MessageBox.showinfo("insert status","All field are required")
    else:
        con=mysql.connect(host="localhost",user="root",password="root", database="pythondb")
        cursor=con.cursor()
        cursor.execute("insert into student1 values('"+ id +"','"+ name +"','"+ number +"','"+ email +"')")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_number.delete(0, 'end')
        e_email.delete(0, 'end')
        
        MessageBox.showinfo("insert status","insert success")
        con.close();
def delete():
    if(e_id.get()==""):
        MessageBox.showinfo("Delete status","id is compulsory for delete")
    else:
        con=mysql.connect(host="localhost",user="root",password="root", database="pythondb")
        cursor=con.cursor()
        cursor.execute("delete from student1 where id='"+ e_id.get() +"'")
        cursor.execute("commit");

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_number.delete(0, 'end')
        e_email.delete(0, 'end')
        
        MessageBox.showinfo("delete status","delete success")
        con.close();
def updatename():
    if(e_id.get()==""):
        MessageBox.showinfo("Update","id is compulsory for update")
    else:
        con=mysql.connect(host="localhost",user="root",password="root",database="pythondb")
        cursor=con.cursor()
        cursor.execute("update student1 set name='"+e_name.get()+"' where id='"+ e_id.get()+"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_number.delete(0, 'end')
        e_email.delete(0, 'end')

        MessageBox.showinfo("Update status","Update Success")
        con.close();
def updatenumber():
    if(e_id.get()==""):
        MessageBox.showinfo("Update","id is compulsory for update")
    else:
        con=mysql.connect(host="localhost",user="root",password="root",database="pythondb")
        cursor=con.cursor()
        cursor.execute("update student1 set number='"+e_number.get()+"' where id='"+ e_id.get()+"'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_number.delete(0, 'end')
        e_email.delete(0, 'end')

        MessageBox.showinfo("Update status","Update Success")
        con.close();


root=Tk()
root.geometry("600x400")
root.title("project")
root.configure(bg='teal')
id=Label(root,text='Enter Id',font=('bold',10),bg='pink')
id.place(x=20,y=30)
name=Label(root,text='Enter Name',font=('bold',10),bg='pink')
name.place(x=20,y=60)
number=Label(root,text='Enter number',font=('bold',10),bg='pink')
number.place(x=20,y=90)
email=Label(root,text='Enter email',font=('bold',10),bg='pink')
email.place(x=20,y=120)
e_id=Entry()
e_id.place(x=150,y=30)
e_name=Entry()
e_name.place(x=150,y=60)
e_number=Entry()
e_number.place(x=150,y=90)
e_email=Entry()
e_email.place(x=150,y=120)
insert=Button(root,text="insert",font=("italic",10),bg="yellow",command=insert)
insert.place(x=20,y=140)
delete=Button(root,text="delete",font=("italic",10),bg="yellow",command=delete)
delete.place(x=20,y=180)
updatename=Button(root,text="update name",font=("italic",10),bg="yellow",command=updatename)
updatename.place(x=20,y=220)
updatenumber=Button(root,text="update number",font=("italic",10),bg="yellow",command=updatenumber)
updatenumber.place(x=20,y=260)
root.mainloop()
