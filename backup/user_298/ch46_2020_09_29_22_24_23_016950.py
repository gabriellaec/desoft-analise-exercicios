numeros = []
corretos = []
def numero_no_indice(numeros):
    x = 0
    while x <= len(numeros):
        if x in numeros:   
            if numeros[x] == numeros.index(x):
                corretos.append(x) 
        x += 1
    return corretos