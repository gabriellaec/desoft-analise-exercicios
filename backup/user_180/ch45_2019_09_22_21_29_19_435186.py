def zera_negativos(lista):
    novalista = []
    for i in lista:
        if i < 0:
            novalista.append(0)
        else:
            novalista.append(i)
    print(novalista)
        