def acha_bigramas(string):
    bigrama = []
    a = string
    if len(a)>=2:
        i = 0
        while i<len(a)-1:
            bigrama.append(a[i]+a[i+1])
            i += 1
        i = 0
        j = 0
        while i<len(bigrama):
            while j<len(bigrama):
                if bigrama[j] == bigrama[i]:
                    del bigrama[j]
                j += 1
            i += 1     
    return bigrama