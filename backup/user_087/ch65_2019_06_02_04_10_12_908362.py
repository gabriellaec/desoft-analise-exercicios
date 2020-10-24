def acha_bigramas(palavra):
    lista = []
    i = 0
    while i < len(palavra):
        lista.append(palavra[i:i+2])
        
        if len(palavra[i:i+2]) == 1:
            lista.remove(palavra[i:i+2])
        i += 1
    listanova = set(lista)

    return listanova


