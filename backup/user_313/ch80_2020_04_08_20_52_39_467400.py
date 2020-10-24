def interseccao_chaves(l1,l2):

    lista= []
    for k in l1:
        lista.append(k)

    novalista= []
    conta = 0
    for i in l2:
        if i == lista[conta]:
            novalista.append(i)
            conta = conta + 1
        
        else:
            conta = conta + 1

    return novalista