a=int(input("Enetr the number"))
s=0
for i in range(1,a):
    if a%i==0:
        print(i)
        s=s+i
if s==a:
    print("perfect")
