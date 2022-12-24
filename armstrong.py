a=int(input("Enter any number"))
dig=0
temp=a
s=0
while a>0:
    dig=a%10
    s=s+dig*dig*dig
    a=a//10
if temp==s:
    print("armstrong number")
else:
    print("not armstrong")
