def verifica_primos(x):
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True
    
def primos_entre(a,b):
    lista = []
    if a < 2:
        i = 2
    else:
        i = a
    while i <= b:
        if verifica_primos(i):
            lista.append(i)
        i += 1
    return lista