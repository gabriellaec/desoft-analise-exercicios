def classifica_lista(lista):
    if len(lista) <= 1:
        return "nenhum"
    
    lista2 = lista.sort()
    print(lista)
    print(lista2)
    if lista == lista2:
        return "crescente"
    
    lista3 = lista.sort(reverse=True)
    if lista == lista2:
        return "decrescente"
    else:
        return "nenhum"