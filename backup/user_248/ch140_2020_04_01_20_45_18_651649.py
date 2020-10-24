def faixa_notas(lista):
    lista=[3, 4, 5, 5.5, 6, 9]
    i=0
    a=0
    b=0
    c=0
    while i<len(lista):
        if lista[i]<5:
            a+=1
        elif lista[i]>5 and lista[i]<7:
            b+=1
        elif lista[i]>7:
            c+=1
            
            