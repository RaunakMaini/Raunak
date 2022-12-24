a=int(input("enter any number"))
count=0
c=a%10
d=a//10
temp=a
while a>0:
    b=a%10
    a=a//10
    count=count+1
t=d*10+b
f=t-(b*(10**(count-1)))
m=f+c*10**(count-1)
print(temp,"reversed number is",m)
