def subtracao_de_listas(listaUm, listaDois):
    lista=[]
    a = len(listaUm)
    b = len(listaDois)
    x = 0
    while x<a:
        c=0
        y=0
        while y<b:
            if listaUm[x] != listaDois[y]:
                c=c+1
                y=y+1
            else:
                y=y+1
        if b == c:
            lista.append(listaUm[x])
            x=x+1
        else:
            x=x+1
    return lista