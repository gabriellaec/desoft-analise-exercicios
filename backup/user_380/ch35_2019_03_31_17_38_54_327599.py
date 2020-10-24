d = float(input())
m = float(input())
t = float(input())
total = d 
for i in range(24):
    d = d * (1+t) + m
    print("{0:.2f}".format(d)) 
print("{0:.2f}".format(d - total - 24 * m))
