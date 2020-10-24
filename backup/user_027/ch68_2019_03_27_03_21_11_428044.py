def separa_trios(x):
    lista = []
    qtd = int(len(x)/3)
    i = 0
    while i < qtd:
        lista.append(x[3*i:3*(i+1)])
        i += 1
    if 3*qtd < len(x):
        lista.append(x[(3*qtd+1):])
    return lista
        