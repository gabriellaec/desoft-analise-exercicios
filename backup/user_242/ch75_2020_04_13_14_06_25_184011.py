def eh_primo (n):
    if n < 2: 
        return False
    
    elif n == 2:
        return True
    
    for x in range(2,n):
        if n % x == 0:
            return False
        
    return True 

def verifica_primos(lista):
    dicionario ={}
    for n in lista:
        dicionario[n] = eh_primo(n)
    return dicionario
