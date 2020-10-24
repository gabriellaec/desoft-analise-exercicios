def verifica_primos(lista):
    i=0
    primos={}
    while i < len(lista):
        if lista[i]%lista[i]==0:
           	primos["{}".format(lista[i])]=True
        else:
            primos["{}".format(lista[i])]=False
        i=1+i
    return primos