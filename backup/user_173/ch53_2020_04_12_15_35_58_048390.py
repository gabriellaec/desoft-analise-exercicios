def numero_impar (x):
    if x%2 == 1:
        return True
    else:
        return False

def soma_impares (lista):
    si = 0
    for i in lista:           
        lista [i] = numero_impar(i)
        si += si + lista[i]
           
    return si
        