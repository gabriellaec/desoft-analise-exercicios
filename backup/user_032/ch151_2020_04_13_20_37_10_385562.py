def classifica_lista(lista): 
    for i in lista:
        if lista[i+1] < lista [i]:
            return "decrescendo"
        elif lista[i+1] > lista[i]:
            return "crescendo"
        else:
            return 'nenhum'