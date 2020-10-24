d = float(input())
a = d
m = float(input())
t = float(input())

for i in range(24):
    d = d*(1+t) + m
    print("{0:.2f}".format(d)) 
print("{0:.2f}".format(d - a - 24 * m))
