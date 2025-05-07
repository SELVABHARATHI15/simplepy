class reverse_num:
    def __init__(self,num):
        self.num = num
    def reverse(self,num):
        rev = 0
        while num > 0:
            rem = num % 10
            rev = rev * 10 + rem
            num = num // 10
        return rev
num = int(input("Enter the number:"))
a = reverse_num(num)
print("The reverse of the number is:",a.reverse(num))