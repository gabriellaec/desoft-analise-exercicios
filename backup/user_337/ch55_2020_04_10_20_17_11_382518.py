def encontra_maximo(matriz):
    linha1 = matriz[0]
    linha2 = matriz[1]
    linha3 = matriz[2]
    i = 0
    while i < len(linha1):
        if linha1[i]<0:
            linha1[i] = linha1[i]*(-1)
        i+=1
    m = 0
    while m < len(linha2):
        if linha2[m]<0:
            linha2[m] = linha2[m]*(-1)
        m+=1
    n = 0
    while n< len(linha3):
        if linha3[n]<0:
            linha3[n] = linha3[n]*(-1)
        n+=1
    v1 = linha1[0]
    v2 = linha2[0]
    v3 = linha3[0]
    for i in linha1:
        if i > v1:
            v1 = i
    for a in linha2:
        if a > v2:
            v2 = a
    for b in linha3:
        if b > v3:
            v3 = b
    if v1 == 0 and v2 == 0 and v3 == 0:
        return v1
    if v1>v2 and v1>v3:
        return v1
    if v2>v1 and v2>v3:
        return v2
    if v3>v1 and v3>v2:
        return v3