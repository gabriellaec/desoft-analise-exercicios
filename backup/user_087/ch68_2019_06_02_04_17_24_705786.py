def separa_trios(lista):
    lista_trios = []
    i = 0
    multiplicador = 1
    while i < len(lista):
        lista_trios.append(lista[i:i+3])
        i = 3*multiplicador
        multiplicador += 1
    i += 1
    
    return lista_trios

