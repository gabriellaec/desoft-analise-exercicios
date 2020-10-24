def classifica_lista(lista):
    j=0
    if len(lista)<2:
        return "nenhum"
    for j in range(len(lista)):
            if lista[j]<lista[j+1]:
                return "crescente"
            elif lista[j]>lista[j+1]:
                return "decrescente"
            elif lista==[]:
                return "nenhum"
            else:
                return "nenhum"