def separa_trios(lista_A):
    i=0
    lista_trios=[]
    while i < len(lista_A):
        lista_trios.append(lista_A[i:i+3])
        i+=3
    return lista_trios
        
        