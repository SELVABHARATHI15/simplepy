a = int(input("Enter the number:"))
rev = 0
n = a
while a != 0:
    rem = a % 10
    rev = rev * 10 + rem
    a = a // 10
print("The number is:",n-rev)
