import math 
  
lista = [0] * 10
 
def Munchhausen(n) : 
    sm = 0
  
    while (n) : 
        sm= sm + lista[(n % 10)] 
        n = n // 10
      
    return (sm == n) 
  
def verifica_numero(n) : 
    for i in range(0, 10) : 
        lista[i] = math.pow((float)(i), (float)(i)) 
    
    for i in range(1,n+1) : 
        if (Munchhausen(i)) : 
            return True
        else:
            return False