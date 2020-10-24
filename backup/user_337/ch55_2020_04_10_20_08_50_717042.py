def encontra_maximo(matriz):
    linha1 = matriz[0]
    linha2 = matriz[1]
    linha3 = matriz[2]
    for x in linha1:
        if x<0:
            x = x*(-1)
    for y in linha2:
        if y<0:
            y = y*(-1)
    for z in linha3:
        if z<0:
            z = z*(-1)
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
    if v1>v2 and v1>v3:
        return v1
    if v2>v1 and v2>v3:
        return v2
    if v3>v1 and v3>v2:
        return v3