def classifica_lista(lista):
    if len(lista)<2:
        return("nenhum")
    n=0
    while n<len(lista)-1:
        if lista[n+1]>lista[n] or lista[n+1]<lista[n]:
            n+=1
        else:
            return ("nenhum)
    i=0
    while i<len(lista)-1:
        if lista[i+1]>lista[i]:
            i+=1
        elif lista[i+1]<lista[i]:
            i+=1
        else:
            return("nenhum")
        return ("decrescente")
    return ("crescente")