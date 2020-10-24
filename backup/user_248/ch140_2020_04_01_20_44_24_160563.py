def faixa_notas(lista):
    lista=[3, 4, 5, 5.5, 6, 9]
    i=0
    n=0
    while i<len(lista):
        if lista[i]<5:
            n+=1
        elif lista[i]>5 and lista[i]<7:
            