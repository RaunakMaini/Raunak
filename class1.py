num=int(input("enter the number you want to search"))
class linear:
    def __init__(self,n):
        self.num=n
    def search(self):
        f=0
        l=[1,2,3,5,4,9,10]
        for i in range(0,len(l)):
            if l[i]==self.num:
                f=1
                break
        if f==1:
            print("element found",l[i],"at position",i+1)
        else:
            print("elemnent not found")
obj=linear(num)
obj.search()
