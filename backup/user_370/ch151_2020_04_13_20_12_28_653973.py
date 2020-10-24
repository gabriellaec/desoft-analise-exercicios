def classifica_lista(lista):
    i=1
    for i in lista:
        if lista[i+1]>lista[i]:
            return "crescente"
        elif lista[i]>lista[i+1]:
            return "decrescente"
        elif lista[i+1]>lista[i] and lista[i]>lista[i+1]:
            return "nenhum"
        elif len(lista)< 2:
            return "nenhum"
        i+=1


            