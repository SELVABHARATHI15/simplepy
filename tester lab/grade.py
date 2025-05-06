s1 =eval(input("enter the mark 1:"))
s2 =eval(input("enter the mark 2:"))
s3 =eval(input("enter the mark 3:"))
s4 =eval(input("enter the mark 4:"))
s5 =eval(input("enter the mark 5:"))
sump =s1+s2+s3+s4+s5
avg =sump/5
print("the average is:",avg)
if avg>=95:
    print("grade s")
elif avg>=90:
    print("grade a")
elif avg>=80:
    print("grade b")
elif avg>=70:
    print("grade c")
elif avg>=60:
    print("grade d")
else:
    print("fail")