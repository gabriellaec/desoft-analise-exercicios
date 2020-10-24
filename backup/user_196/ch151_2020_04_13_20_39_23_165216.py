def classifica_lista(lista):
    anterior = lista[0]
    for proximo in lista:
        if proximo < anterior:
            print ("decrescente")
        elif proximo > anterior:
            print ("crescente")
        else:
            print("nenhum")
    if len(lista)<2:
        print ("nenhum")