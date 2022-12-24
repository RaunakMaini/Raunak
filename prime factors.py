a=int(input("Enetr the number"))
b=0
flag=False
for i in range(1,a+1):
    if a%i==0:
        for j in range(2,a):
            if a%j==0:
    
                flag=True
                break
if flag:
    print("not")
else:
    print("yes")
