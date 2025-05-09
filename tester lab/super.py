class person:
    def __init__(self,name):
        self.name = name
    def hello(self):
        return f"Hello {self.name}"
class member(person):
    def __init__(self,name):
        super().__init__(name)
cla = member("john snow")
print(cla.hello())