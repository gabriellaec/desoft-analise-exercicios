def apaga_repetidos(string):
    lista = []*len(string)
    i=0
    while i<len(string):
        if string[i] not in lista:
            lista.append(string[i])
        else:
            lista.append('*')
            
    frase = lista[0]
    j = 1
    while j < len(lista):
        frase += lista[j]
        j+=1
    return frase
            