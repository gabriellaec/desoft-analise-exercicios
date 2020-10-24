def verifica_primos(lista):
    i=0
    lista_1=[]
    while i < len(lista):
        if lista[i]==2:
            lista_1.append(True)
            i+=1
        if lista[i]==0 or lista[i]==1:
            lista_1.appen(False)
            i+=1
        if lista[i]%2==0:
            lista_1.append(False)
            i+=1
        x=3
        while x<lista[i]:
            if lista[i]%x==0:
                lista_1.append(False)
                i+=1
            x+=2
        lista_1.append(True)
        i+=1
    dicionario=dict(zip(lista, lista_1))
    return dicionario