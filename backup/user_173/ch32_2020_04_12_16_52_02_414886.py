def numero_primo (x):
    if x <= 1:
        return False
    
    for i in range(2,x):
        if x%i == 0:
            return False
       
    return True

def lista_primos (n):
    lista = []
    i = 0
    while i < n:
        lista[i] = numero_primo(i)
        i += 1
    return lista    