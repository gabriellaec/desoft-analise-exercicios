def conta_bigramas(palavra):
    dicio = {}
    lista = []
    p1 = palavra[0]
    p2 = palavra[1]
    soma = p1+p2
    lista.append(soma)
    for p in range(2, len(palavra)):
        soma = p2 + palavra[p]
        lista.append(soma)
        p2 = palavra[p]
    i=0
    while i <len(lista):
        b=0
        c=0
        while b<len(lista):
            if lista[i] == lista[b]:
                c+=1
                b+=1
            else:
                b+=1
        dicio[lista[i]] = c
        i+=1
    return dicio