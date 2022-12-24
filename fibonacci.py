a=int(input("Enter any number"))
n1=0
n2=1
count=0
if a<0:
    print("not possible")
elif a==1:
    print(n1)
else:
    while count<a:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
