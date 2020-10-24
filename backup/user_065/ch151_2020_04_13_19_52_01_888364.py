def classifica_lista(lista):
    is len(lista) < 2:
        return "nenhum"
    
    lista2 = lista.sort()
    if lista == lista2:
        return "crescente"
    
    lista3 = lista.sort(reverse=True)
    if lista == lista2:
        return "decrescente"
    else:
        return "nenhum"