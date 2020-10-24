def separa_trios(x):
    lista = []
    qtd = int(len(x)/3)
    i = 0
    while i < qtd:
        lista.append(x[3*i:3*(i+1)])
        i += 1
    lista.append(x[i*3 :])
    return lista

