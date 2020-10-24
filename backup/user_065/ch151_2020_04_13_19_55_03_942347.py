def classifica_lista(lista):
    if len(lista) < 2:
        return "nenhum"
    
    lista2 = lista.sorted()
    print(lista)
    print(lista2)
    if lista == lista2:
        return "crescente"
    
    lista3 = lista.sorted(reverse=True)
    if lista == lista2:
        return "decrescente"
    else:
        return "nenhum"