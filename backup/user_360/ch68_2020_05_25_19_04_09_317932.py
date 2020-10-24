def separa_trios(lista):
    lista2 = []
    i = 0
    while i<len(lista):
        lista[i:i+3].append(lista2)
    i+=3
    return lista2    
        
        