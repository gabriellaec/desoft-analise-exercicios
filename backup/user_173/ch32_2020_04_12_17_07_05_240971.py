def numero_primo (x):
    if x <= 1:
        return False
    
    for i in range(2,x):
        if x%i == 0:
            return False
       
    return True

def lista_primos (n):
    lista1 = [0]*n
    a = 1
    i = 0
    lista2 = []
    while i < len(lista1):
        lista1[i] = a
        if numero_primo(lista1[i]) == True:
            lista2.append (lista1[i])
        i += 1
        a += 1
    return lista2    