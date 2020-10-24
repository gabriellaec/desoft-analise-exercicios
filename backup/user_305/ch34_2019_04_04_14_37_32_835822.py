a = float(input('quanta grana vc colocou?'))
b = float(input('quanto de taxa consagration?'))
m = 0
y = a + a*b/100
print ('{0:.2f}'.format(y))
while m < 24:
    y += y*b/100
    m+=1
    print (y)

print('{0:.2f}'.format(y- a + a*b/100))
