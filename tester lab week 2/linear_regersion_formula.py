week =[1,2,3,4,5]
sales = [1.2,1.8,2.6,3.2,3.8]
sx,sy,sx2,sxy = 0,0,0,0
for i in range(len(week)):
    sx = sx + week[i]
    sy = sy + sales[i]
    sx2 = sx2+week[i] * week[i]
    sxy = sxy + week[i] * sales[i]
ax = sx / len(week)
ay = sy / len(week)
ax2 = sx2 / len(week)
axy = sxy / len(week)
a1 =(axy - ax * ay) / (ax2 - ax * ax)
a0 =(ay - a1 * ax)
print(f"{a1:.2f}x + {a0:.2f}")