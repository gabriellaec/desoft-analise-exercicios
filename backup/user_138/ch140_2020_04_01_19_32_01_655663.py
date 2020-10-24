def faixa_notas(lista):
    l=len(lista)
    a=0
    b=0
    c=0
    while a>1:
        if lista[b]<5:
            return lista[a]
        elif lista[b]<=7:
            return lista[b]
        else:
            return lista[c]
        b+=1