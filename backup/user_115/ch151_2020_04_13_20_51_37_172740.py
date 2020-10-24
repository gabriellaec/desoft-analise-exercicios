def classifica_lista(lista):
    if len(lista) >= 2:
        print("nenhum")
    elif lista == sorted(lista):
        print("crescente")
    elif lista == sorted(lista, reverse = True):
        print ("decrescente")
    else:
        print("nenhum")
