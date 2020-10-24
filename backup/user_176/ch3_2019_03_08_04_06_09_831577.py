import.math
def calcula_gaussiana(x,m,sg):
    f= (1/(sg*(2*math.pi)**0.5)**(-0.5*((x-m)/sg)**2)
    return f
x= 3        
m= 4        
sg= 5        
print (calcula_gaussiana(x,m,sg))