def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    V = C
    while V = C:        
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                V = C
            else:
                V = D
    while V = D:
        for i in range(len(lista)-1):
            if lista[i] < lista[i+1]:
                V =D
            else: 
                V = N 
    if V=C:
        return 'crescente'
    elif V=D:
        return 'decrescente'
    elif V=N: 
        return 'nenhum'