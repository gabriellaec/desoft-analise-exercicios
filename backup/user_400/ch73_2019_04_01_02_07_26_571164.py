def remove_vogais(PALAVRA):
    i = 0
    k = 0
    j = 0
    lista = []
    while i < len(PALAVRA):
        lista.append(PALAVRA[i])
        i += 1
    while k < len(lista):
        if lista[k] == "a" or lista[k] =="e" or lista[k] == "i" or lista[k] == "o" or lista[k] == "u":
            del lista[k]
            k += 1
        else:
            k += 1
    while j + 1 < len(lista):
        lista[0] += lista[j]
        j += 1
    return lista[0]
    
    