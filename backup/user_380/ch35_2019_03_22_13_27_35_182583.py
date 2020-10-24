d = float(input())
e = float(input())
j = float(input())

g = 0

for i in range(24):
    g += d*(1+j)
    
    if i >= 2:
    	d = d*(1+j)+e
    else:
        d = d*(1+j)
        
    print("{0:.2f}".format(d))
    
print("{0:.2f}".format(g))