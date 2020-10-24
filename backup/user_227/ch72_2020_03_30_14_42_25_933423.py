def lista_caracteres(s):
    lista = list(s)
    caracteres = []
    i = 0
    while i < len(lista):
        if lista[i] in caracteres:
            i += 1
        
        else:
            caracteres.append(lista[i])
            i += 1
    
    return caracteres