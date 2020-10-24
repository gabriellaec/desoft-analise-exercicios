
def numero_no_indice(numeros):
    corretos = []
    x = 0
    while x < len(numeros):   
        if numeros[x] == numeros.index(numeros[x]):
                corretos.append(x) 
        x += 1
    return corretos