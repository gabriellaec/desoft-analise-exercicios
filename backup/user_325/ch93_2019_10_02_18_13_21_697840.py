import math 
  
lista = [0] * 10
 
def Munchhausen(n) : 
    som = 0
  
    while (n) : 
        som= som + lista[(n % 10)] 
        n = n // 10
      
    return (som == n) 
  
def verifica_numero(n) : 
    for i in range(0, 10) : 
        lista[i] = math.pow((float)(i), (float)(i)) 
    
    for i in range(1,n+1) : 
        if (Munchhausen(i)) : 
            return True
        else:
            return False