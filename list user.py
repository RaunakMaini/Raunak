a=[]
b=int(input("enter the number of elements you want to enter"))
for i in range(0,b):
    c=input("enter the element")
    a.append(c)
print(a)
d=int(input("enter the option \n 1. input \n 2.delete"))
if d==1:
    pos=int(input("enter the position"))
    dat=int(input("enter the data"))
    a.insert(pos+1,dat)
    print(a)
if d==2:
    pos=int(input("enter the position"))
    a.pop(pos-1)
    print(a)
