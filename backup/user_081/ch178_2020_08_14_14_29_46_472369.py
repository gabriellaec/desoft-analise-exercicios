def junta_nomes(x,y,z):
    lista = []
    for i in x:
        for j in z:
            nova = i + ' '+j:
            if nova not in lista:
                lista.append(nova)
    for k in y:
        for l in z:
            nova1 = k + ' '+l
            if nova1 not in lista:
                lista.append(nova1)
    print(lista)