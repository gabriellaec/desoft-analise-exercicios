def separa_trios(lista):
    
    i = 0
    trios = []
    while i < len(lista):
        novo = lista[i:i+3]
        trios.append(novo)
        i+= 3
    return trios
