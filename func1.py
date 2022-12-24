def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def cube(*a):
    for i in a:
        i=int(i)
        print(i*i*i)
def circle(r):
    
    while True:
        a=int(input("choose any option\n 1. diameter\n2.circumference\n3.area\n4. press 0 for exit"))
        if a==1:
            dia=2*r
            print(dia)
        elif a==2:
            cir=2*3.14*r
            print(cir)
        elif a==3:
            area=3.14*r*r
            print(area)
        elif a==0:
            break
        else:
            print("invalid input")
def arm(num):
    num=int(input("enter any number"))
    s=0
    temp=num
    while num>0:
        b=num%10
        s=s+b*b*b
        num=num//10
    if temp==s:
        print("armstrong number")
    else:
        print("not armstrong")
c=int(input("Enter any number"))
d=int(input("Enter any number"))
num=int(input("choose the operationn you want to perform\n1.add\n2.sub\n3.cube\n4. circle info \n 5. armstrong"))
if num==1:
    add(c,d)
elif num==2:
    sub(c,d)
elif num==3:
    cube(c,d,c)
elif num==4:
    circle(r=5)
elif num==5:
    arm(num)
