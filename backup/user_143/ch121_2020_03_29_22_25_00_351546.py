def subtracao_de_listas(lista1, lista2):
    d=len(lista1)
    f=len(lista2)
    lista=[]
    i=0
    while i<d:
        a=0
        b=0
        while b<f:
            if lista1[i]!=lista2[a]:
                a+=1
                b+=1
            else:
                b+=1
        if b==a:
            lista.append(lista[i]
            i+=1
        else:
            i+=1
    return lista