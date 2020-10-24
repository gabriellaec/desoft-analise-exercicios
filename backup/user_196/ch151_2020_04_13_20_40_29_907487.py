def classifica_lista(lista):
    for i in range (len(lista)):
        if lista[i] < lista[i-1]:
            print ("decrescente")
        elif lista[i] > lista[i+1]:
            print ("crescente")
        else:
            print("nenhum")
    if len(lista) < 2:
        print ("nenhum")