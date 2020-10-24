def monta_mala(lista):
    i=0
    somavalores=0
    listanova=[]
    while i<len(lista):
        somavalores+=lista[i]
        if somavalores <= 23:
            print(somavalores)
            listanova.append(lista[i])
            i+=1
        else:
            break
    return listanova