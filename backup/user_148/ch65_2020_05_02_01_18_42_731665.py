def capitaliza(str):
    lista = [0]*len(str)
    lista[0] = str[0].upper()
    i = 1
    while i<len(str):
        lista[i] = str[i]
        i += 1
    return ''.join(lista)