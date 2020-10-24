def calcula_media(lista):
    listaval=[]
    for x in lista:
        for val in x.values():
            listaval.append(val)
    x=len(listaval)
    y=sum(listaval)
    media=y/x
    return media