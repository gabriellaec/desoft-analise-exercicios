
def numero_no_indice(numeros):
    corretos = []
    x = 0
    while x < len(numeros):   
        if numeros[x] == x:
                corretos.append(x) 
        x += 1
    return corretos