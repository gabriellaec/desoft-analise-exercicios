depo = float(input())
tax = float(input())
tax = tax/100

tet = 0
tot = 0

t = 24

while t > 0: 
    
    print('{0:.2f}'.format(depo))
    
    tot = depo * (tax - 1)
    tet+= tot
    
    depo *= tax
    
    t -= 1
    
print('{0:.2f}'.format(tet))
    
    
