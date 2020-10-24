def eh_primo(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
  
def lista_primos(n):
    lista=[]
    i=0
    a=0
    while i<n:
        if eh_primo(a):
            lista.append(a)
            i+=1
            a+=1
            lista.sort()
        else:
            a+=1
    return lista
        
  
  