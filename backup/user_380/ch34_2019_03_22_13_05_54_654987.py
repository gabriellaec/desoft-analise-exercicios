d = float(input())
j = float(input())
for i in range(24):
    d += d*(1+j)
    print("{0:.2f".format(d))
