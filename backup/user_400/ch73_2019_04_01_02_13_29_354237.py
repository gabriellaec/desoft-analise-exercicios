def remove_vogais(PALAVRA):
    i = 0
    k = 0
    j = 1
    lista = []
    lista2 = []
    while i < len(PALAVRA):
        lista.append(PALAVRA[i])
        i += 1
    while k < len(lista):
        if lista[k] == "a" or lista[k] == "e" or lista[k] == "i" or lista[k] == "o" or lista[k] == "u":
            k += 1
        else:
            lista2.append(lista[k])
            k += 1
    while j < len(lista2):
        lista2[0] += lista2[j]
        j += 1
    if len(lista2) == 0:
        return ""
    else:
        return lista2[0]
    
    