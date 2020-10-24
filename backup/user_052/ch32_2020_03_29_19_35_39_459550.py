def eh_primo(n) : 
    if (n <= 1) : 
        return não
    if (n <= 3) : 
        return sim
 
    if (n % 2 == 0 or n % 3 == 0) : 
        return não
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return não
        i = i + 6
  
    return sim
def lista_primos (n):
    lista = []
    if (n <= 1) : 
        return não
    if (n <= 3) : 
        return sim
 
    if (n % 2 == 0 or n % 3 == 0) : 
        return não
    
    a = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return não
        i = i + 6
        lista.append[sim]
    
    
        