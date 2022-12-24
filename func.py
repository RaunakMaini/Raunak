def add():
    a=int(input("enter: "))
    b=int(input("enter: "))
    print(a+b)
def sub():
    a=int(input("enter: "))
    b=int(input("enter: "))
    print(a-b)
def mul():
    a=int(input("enter: "))
    b=int(input("enter: "))
    print(a*b)
def div():
    a=int(input("enter: "))
    b=int(input("enter: "))
    print(a/b)
def power():
    a=int(input("enter: "))
    b=int(input("enter: "))
    print(a**b)
c=int(input("1-add\n 2-sub\n 3-mul\n 4-div\n 5-power"))
if(c==1):
    add()
elif(c==2):
    sub()
elif(c==3):
    mul()
elif(c==4):
    div()
elif(c==5):
    power();
