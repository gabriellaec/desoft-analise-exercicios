depo = float(input())
tax = float(input())
tax = tax/100 + 1
dep = depo

tet = 0
tot = 0

t = 24

while t > 0: 
    
    print('{0:.2f}'.format(depo))
    
    depo *= tax
    
    
    
 
    
    t -= 1
    
print('{0:.2f}'.format(depo - dep))
    
    
