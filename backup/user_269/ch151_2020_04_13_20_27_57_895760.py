def classifica_lista(lista):
    for e in range(len(lista)):
        if len(lista)==2:
            print("nenhum")
        elif lista[0]+len(lista)-1==lista[len(lista)-1]:
            print("crescente")
        elif lista[len(lista)]+len(lista)-1==lista[0]:
            print("decrescente")
        else:
            print("nenhum")