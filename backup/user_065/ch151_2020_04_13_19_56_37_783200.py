def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    
    lista2 = sorted(lista)
    if lista == lista2:
        return "crescente"
    
    lista3 = sorted(lista, reverse=True)
    if lista == lista3:
        return "decrescente"
    else:
        return "nenhum"