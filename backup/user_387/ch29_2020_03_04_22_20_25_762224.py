depo = float(input())
tax = float(input())
sald = dep
t = 1

while t <= 24: 
    
    sald = sald + (sald * (tax / 100)
    
    print('{0},{1:.2f}'.format(t, sald))
    
    t += 1
    
print('{0:.2f}'.format(sald - depo))
    
    
