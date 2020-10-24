def acha_bigramas(a):
    resultado = []
    i = 0
    while i < len(a)-1:
        resultado.append(a[i]+a[i+1])
        i += 1
        
    return resultado