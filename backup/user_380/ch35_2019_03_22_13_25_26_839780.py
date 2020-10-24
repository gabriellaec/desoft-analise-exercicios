d = float(input())
e = float(input())
s = d
g = 0
j = float(input())
for i in range(24):
    g += d*(1+j)
    d = d*(1+j)+e
    print("{0:.2f}".format(d))
print("{0:.2f}".format(g))