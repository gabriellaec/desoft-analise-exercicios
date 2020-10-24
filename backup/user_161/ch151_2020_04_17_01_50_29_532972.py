def classifica_lista(lista):
    a=True
    b=True
    i=0
    if lista==[] or len(lista)==1:
        return "nenhum"
    while i<len(lista)-1:
        if lista[i+1]>lista[i]:
            a=False
            i+=1
        elif lista[i+1]<lista[i]:
            b=False
            i+=1
    if a:
        return "decrescente"
    elif b:
        return "crescente"
    else:
        return "nenhum"