def calcula_media(lista):
    x=[]
    for i in lista:
        for e,v in i.items():
            x.append(v)

    return sum(x)/len(x)