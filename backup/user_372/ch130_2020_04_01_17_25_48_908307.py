def monta_mala(lista):
    peso=int(input('Peso item: '))
    soma=0
    i=0
    lista=[]
    lista.append(peso)
    while soma<=23:
        soma+=lista[i]
        i+=1
    else:
        del lista[i] 