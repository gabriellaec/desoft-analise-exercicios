lista = [1,5,-3,-9,2,5,-8]

def zera_negativos(x):
    while indice < len(x):
        if x[indice] < 0:
        	x[indice] = 0
        	indice = indice + 1
        else:
        	indice = indice + 1
    return x

print (zera_negativos(lista))