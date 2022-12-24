a=int(input("Enter any number"))
maxx=0
while a>0:
    b=a%10
    if maxx<b:
        maxx=b
    else:
        a=a//10
print(maxx)
