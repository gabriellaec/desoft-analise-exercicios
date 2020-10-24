import math
def arcotangente(x,n):
    
    n_1=0
    n_2=0
    
    i=1
    contador=0
    while contador != n:
        if contador %2==0:
            n_1 += (x**i)/i
            
        else:
            n_2 += ((x*i)/i)-1

        i+=2
        contador+=1
        
    y=n_1+n_2*(math.pi/180)
    
    return y