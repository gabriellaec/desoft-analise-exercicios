def numero_primo (x):
    if x <= 0:
        return False
    
    for i in range(2,x):
        if x%i == 0:
            return False
       
    return True

def verifica_primos (lista):
    dicionario = {}
    
    for item in lista:
        dicionario[item] = numero_primo(item)
        
    return dicionario
    
    
    