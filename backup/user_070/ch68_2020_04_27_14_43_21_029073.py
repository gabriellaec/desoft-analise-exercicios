def separa_trios(lista):
    trios = []
    for i in range(int(len(lista)/3)):
        trios.append(lista[i*3:i*3+3])
    if len(lista)%3 == 1:
        trios.append([lista[-1]])
    elif len(lista)%3 == 2:
        trios.append([lista[-2],lista[-1]])
    return trios