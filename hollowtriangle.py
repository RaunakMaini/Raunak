a=int(input("enter any number"))
i=0
j=1
while i<a:
    print(" "*(a-i)+"*"*(i-j)+"*"*(i+1+j))
    i=i+1
    j=j+1
    
