def classifica_lista(lista):
    if len(lista)<2:
        return "nenhum"
    i=0
    a=1
    while i<len(lista):
        if lista[i]<lista[a]:
            return "crescente"
            a+=1
        if lista[i]>lista[a]:
            return "decrescente"
            a+=1
        else:
            return "nenhum"
    i+=1