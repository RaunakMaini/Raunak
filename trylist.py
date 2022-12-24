try:
    a=[]
    n=int(input("Enter the size of list"))
    for i in range(0,n):
        value=input("Enter Data")
        a.append(value)
    print("the lisr is",a)
    new=input("new value")
    a[-1]=[new]
    print(a)
except Expception as e:
    print("invalid",e)
