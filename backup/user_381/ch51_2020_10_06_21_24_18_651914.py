def eh_primo(x):
    if x == 1:
        return False
    if x % 2 == 0 and x!=2:
        return False
    i=3
    while i<x:
        if x%i==0:
            return False
        i += 2
    return True

def primos_entre(a, b):
    lista_primos = []
    i = a
    while i >= a and i <= b:
        if eh_primo(i) == True:
            lista_primos.append(i)
        i += 1
    contador = 0
    lista_primos_sem_negativos = []
    while contador < len(lista_primos):
        if lista_primos[contador] > 0:
            lista_primos_sem_negativos.append(lista_primos[contador])
        contador += 1
    return lista_primos_sem_negativos