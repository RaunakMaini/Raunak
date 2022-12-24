a=[]
b=[]
c=int(input("enter the length of list"))
for i in range(0,c):
    d=int(input("enter data"))
    a.append(d)
print(a)
while a:
    m=a[0]
    for i in a:
        if i<m:
            m=i
    b.append(m)
    a.remove(m)
print(b)
