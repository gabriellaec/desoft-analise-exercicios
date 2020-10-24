def separa_trios (lista):
    listanova = []
    i = 0 
    while i < len(lista):
        listanova.append(lista[i:i+3])
        i += 3
    return listanova
    