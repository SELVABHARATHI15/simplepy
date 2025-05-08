n = eval(input("Enter a number: "))
r = eval(input("Enter a range: "))
for i in range(1, r+1):
    print(n, "x", i, "=", n*i)
