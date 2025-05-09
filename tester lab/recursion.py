def rec(num):
    if num == 1:
        return 1
    else:
        return num * rec(num - 1)
n = eval(input("Enter a number: "))
print(rec(n))