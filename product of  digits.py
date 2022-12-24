a=int(input("enter the nunber"))
s=1
while a>0:
    b=a%10
    a=a//10
    s=s*b
print(s)
