class A:
    def __init__(self):
        self._a=10
class B(A):
    def __init__(self):
        A.__init__(self)
        print(self._a)
obj=B()
print(obj.a)
