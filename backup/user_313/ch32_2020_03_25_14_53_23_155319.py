def eh_primo(x):
    if(x == 0 or x == 1):
        return(False)
    if (x == 2):
        return(True)
    if (x%2 == 0):
        return(False)
    
    a = 3
    while a < x:
        if x%a ==0:
            return(False)
        else:
            a = a + 2
    return(True)

def lista_primos(n):
    lista = [0]*n

    t = True
    indice = 0
    contador = 2
    while indice < n:
        if(eh_primo(contador) == True):
            lista[indice] = contador
            indice += 1
        contador += 1
        
    return(lista)

print(lista_primos(5))