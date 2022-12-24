try:
    a=int(input("enter any number"))
    b=int(input("enter any number"))
    print(a/b)
except Exception as e:
    print("invalid",e)
else:
    print("else")
finally:
    print("h")
