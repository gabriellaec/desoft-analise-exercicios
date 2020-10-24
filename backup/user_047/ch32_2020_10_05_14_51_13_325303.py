def eh_primo(x):
    contador = 2
    z = 2
    if x ==2:
        return True
    if x <=1:
        return False  
    while contador < x:
        resto = x%contador
        z = resto
        if z == 0:
            return False
        contador+=1
    return True 


def lista_primos(n): 
    lista = []
    primos = []
    contador = 0 
    while len(primos)<n:
        lista.append(contador+1)
        if eh_primo(lista[contador]):
            primos.append(lista[contador])
        contador+=1
    return primos
       