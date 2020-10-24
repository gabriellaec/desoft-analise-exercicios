x=1
n=6

def arcotangente(x,n):
    
    n_par=0
    n_impar=0
    
    i=1
    contador=1
    while contador != n:
        if contador %2==0:
            n_par += (x**i)/i)
            
        else:
            n_impar += (x**i)/i

        i+=2
        contador+=1
        
    
    return n_impar,n_par