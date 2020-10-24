def mais_populoso(brasil):
    lista=list(brasil.values())
    lista2=list(brasil.keys())
    i=0
    lista4=[]
    while i < len(lista):
        lista1=dict(lista[i])
        lista5=list(lista1.values())
        lista6=sum(lista5)
        lista4.append(lista6)
        i+=1
    brasil_pop=dict(zip(lista2, lista4))
    w=0
    for j in brasil_pop:
        if brasil_pop[j] > w:
            w=brasil_pop[j]
            h=j
    return h