def classifica_lista(lista):
    for i in lista:
        if lista[i]<lista[i+1]:
            return "crescente"
        