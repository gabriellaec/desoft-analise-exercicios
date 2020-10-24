def acha_bigramas(a):
    resultado = []
    i = 0
    while i < len(a)-1:
        if a[i]+a[i+1] not in resultado:
            resultado.append(a[i]+a[i+1])
            i += 1
        else:
            i+ = 1
    return resultado
