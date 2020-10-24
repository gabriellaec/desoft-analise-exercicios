def eh_primo (n):
    if n < 2: 
        return False
    
    elif n == 2:
        return True
    
    for x in range(2,n):
        if n % x == 0:
            return False
        
    return True 

def primos_entre(a,b):
    lista_de_primos = []
    for i in range(a,b+1):
        if eh_primo(i):
            lista_de_primos.append(i)
    return (lista_de_primos)
        