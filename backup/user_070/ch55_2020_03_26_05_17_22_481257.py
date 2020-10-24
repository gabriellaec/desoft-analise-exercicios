def encontra_maximo(matriz):
    linha1 = matriz[0]
    linha2 = matriz[1]
    linha3 = matriz[2]
    maior1 = linha1[0]
    maior2 = linha2[0]
    maior3 = linha3[0]
    i = 1
    while i < 3:
        if linha1[i] > linha1[i-1]:
            maior1 = linha1[i]
        i += 1
    i = 1
    while i < 3:
        if linha2[i] > linha2[i-1]:
            maior2 = linha2[i]
        i += 1
    i = 1
    while i < 3:
        if linha3[i] > linha3[i-1]:
            maior3 = linha3[i]
        i += 1
    if maior1 >= maior2 and maior1 >= maior3:
        return maior1
    elif maior2 >= maior1 and maior2 >= maior3:
        return maior2
    elif maior3 >= maior2 and maior3 >= maior1:
        return maior3