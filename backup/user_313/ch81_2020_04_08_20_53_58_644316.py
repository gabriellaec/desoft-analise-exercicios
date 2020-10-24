def interseccao_valores(l1,l2):

    lista= []
    for k, v in l1.items():
        lista.append(v)

    novalista= []
    conta = 0
    for i in l2.values():
        if i == lista[conta]:
            novalista.append(i)
            conta = conta + 1
        
        else:
            conta = conta + 1

    return novalista