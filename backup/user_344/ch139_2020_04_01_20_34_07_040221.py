import math
def arcotangente(x,n):
    soma = 0
    i= 0
    Positivo = 0
    Negativo = 0
    Expoente = 1
    Dividendo = 1
    
    while i <=n:
        if i % 2 == 1:
            Negativo += (x**(Expoente+2)/(Dividendo+2))
        if i % 2 == 0:
            Positivo += (x**(Expoente)/Dividendo)
        Dividendo+ =2
        Expoente += 2
        i+=1
        Arctg = (x +Positivo - Negativo)*(math.pi/180)
        return Arctg
        
        
    
    
    
