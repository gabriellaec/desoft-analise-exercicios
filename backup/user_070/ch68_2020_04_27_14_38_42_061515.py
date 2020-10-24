def separa_trios(lista):
    trios = []
    for i in range(int(len(lista)/3)):
        trios.append(lista[i:i+3])
    if len(lista)%3 == 1:
        trios.append(lista[-1])
    elif len(lista)%3 == 2:
        trios.append(lista[-1:-3])
    return trios

print(separa_trios(['A0']))