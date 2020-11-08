import.math
def calcula_gaussiana(x,m,sg):
    f= (1/(sg*((2*math.pi)**(1/2)))**((-1/2)*((x-m)**2)/(sg**2))
    return f
x= 3        
m= 4        
sg= 5        
print (calcula_gaussiana(x,m,sg))