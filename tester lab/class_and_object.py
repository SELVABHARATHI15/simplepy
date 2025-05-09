# class addi:
#     def add(self,a,b=0,c=0):
#         return a+b+c
# ad = addi()
# print(ad.add(1,2))
class class_and_object:
    def __init__(self,name,address):
        self.name = name
        self.address = address

    def print_detail(self):
        return (f"Name:{self.name}\n"
                f"Address:{self.address}")

c1 = class_and_object('John','TN-50')
c2 = class_and_object('snowlight','TN-52')

print(c1.print_detail())
print(c2.print_detail())

while True:
    name = input("Enter name:")
    address = input("Enter address:")
    c3 = class_and_object(name,address)
    print(c3.print_detail())