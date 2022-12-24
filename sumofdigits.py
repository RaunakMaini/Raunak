a=int(input("enter the nunber"))
s=0
while a>0:
    b=a%10
    a=a//10
    s=b*10+b+s
print(s)
