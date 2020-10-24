def classifica_lista(lista):
    for i in lista:
        if lista.count(i)>2:
            return 'nenhum'
    maior=lista[0] 
    e=0
    for e in range(len(lista)-1):
        if lista[e+1]>maior:
            maior=lista[e+1]
            return 'crescente'
        elif lista[e+1]<maior:
            maior=menor
            menor=lista[e+1]
            'decrescente'
        else:
            'nenhum'