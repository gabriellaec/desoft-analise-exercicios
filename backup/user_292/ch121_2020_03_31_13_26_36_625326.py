def subtracao_de_listas(lista1,lista2):
    lista=[]
    a=len(lista1)
    b=len(lista2)
    x=0
    while x<a:
        d=0
        y=0
        while y<b:
            if lista1[x]!=lista2[y]:
                d+=1
                y+=1
            else:
                y+=1
        if b==d:
            lista.append(lista[x])
            x+=1
        else:
            x+=1
    return lista