lista_de_numeros = [1, 3, -5, 10, -9, -3, 0, -5]

def zera_negativos(elementos):
    i=0

    while i < len(elementos):
        if elementos[i] < 0:
            elementos[i] = 0
            i += 1
        else:
            i += 1
    
    return elementos

print(zera_negativos(lista_de_numeros))