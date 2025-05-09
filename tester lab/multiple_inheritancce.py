class Add:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a+self.b
class multi:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def multiple(self):
        return self.a*self.b
class add_multi(Add,multi):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addit_multi(self):
        a = Add.addition(self)
        b = multi.multiple(self)
        return a,b
cl = add_multi(1,2)
print(cl.addit_multi())
print(cl.addition())
print(cl.multiple())