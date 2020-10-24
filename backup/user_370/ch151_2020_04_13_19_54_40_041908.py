def classifica_lista(lista):
    for i in lista:
        if lista[i+1]>lista[i]:
            print ("crescente")
        elif lista[i]>lista[i+1]:
            print ("decrescente")
        elif lista[i+1]>lista[i] and lista[i]>lista[i+1]:
            print ("nenhum")
        else:
            print ("nenhum")
            