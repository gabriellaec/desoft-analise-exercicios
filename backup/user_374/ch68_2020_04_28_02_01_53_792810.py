def separa_trios(string):
    lista = []
    i = 0
    while i < len(string):
        lista.append(string[i:i+3])
        i +=3
    
    return lista
    
