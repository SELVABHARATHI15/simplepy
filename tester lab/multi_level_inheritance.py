class one:
    def print1(self):
        return 'one'
class two(one):
    def print2(self):
        return 'two'
class three(two):
    def print3(self):
        return 'three'
class four(three):
    def print4(self):
        return 'four'
obj = four()
print(obj.print1())
print(obj.print2())
print(obj.print3())
print(obj.print4())