class one:
    def one(self):
        return 'one'
class two(one):
    def two(self):
        return 'two'
c = two()
print(c.one())
print(c.two())