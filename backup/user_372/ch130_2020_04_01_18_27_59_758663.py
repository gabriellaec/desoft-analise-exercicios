def monta_mala(lista):
    soma=0
    i=0
    lista=[]
    lista.append(lista[i])
    while soma<=23:
        soma+=lista[i]
        i+=1
    else:
        del lista[i]
