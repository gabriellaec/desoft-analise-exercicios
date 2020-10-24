depo = float(input())
tax = float(input())

tet = 0
tot = 0

t = 24

while t > 0: 
    
    print(depo)
    
    tot = depo * (tax - 1)
    tet+= tot
    
    depo *= tax
    
    t -= 1
    
print()
    
    
