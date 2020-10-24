d = float(input())
s = d
e = float(input())
j = float(input())

for i in range(24):
    d = d*(1+j)+e
    print("{0:.2f}".format(d))
    
print("{0:.2f}".format(d - s - 24*e))