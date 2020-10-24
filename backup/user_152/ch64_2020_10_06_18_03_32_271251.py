def acha_bigramas(string):
    bigrama = []
    a = string
    a = str(a)
    if len(a)>=2:
        i = 0
        while i<len(a)-1:
            bigrama.append(a[i]+a[i+1])
            i += 1
    return bigrama 