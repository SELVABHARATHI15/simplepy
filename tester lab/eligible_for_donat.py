age = eval(input("Enter your age:"))
if(age >= 18):
    weight = eval(input("Enter your weight:"))
    if(weight >= 50):
        print("Eligible for donation")
    else:
        print("Not eligible")
else:
    print("Not eligible")