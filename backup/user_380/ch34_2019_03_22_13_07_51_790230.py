d = float(input())
s = d
j = float(input())
for i in range(24):
    d += d*(1+j)
    print("{0:.2f}".format(d))
print("{0:.2f}".format(d-s))
