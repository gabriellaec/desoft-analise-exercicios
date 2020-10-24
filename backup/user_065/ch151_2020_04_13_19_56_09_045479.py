def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    
    lista2 = sorted(lista)
    print(lista)
    print(lista2)
    if lista == lista2:
        return "crescente"
    
    lista3 = sorted(lista, reverse=True)
    if lista == lista2:
        return "decrescente"
    else:
        return "nenhum"