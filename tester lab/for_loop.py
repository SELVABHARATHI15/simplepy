class Loop:
    def loop(self,n):
        sum1 = 0
        for i in range(1,n+1):
            sum1 += i
        return sum1
n = eval(input())
a = Loop()
print(a.loop(n))