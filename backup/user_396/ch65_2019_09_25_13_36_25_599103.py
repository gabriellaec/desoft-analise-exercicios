def acha_bigramas(x):
    i = 0
    lis = []
    while i < len(x)-1:
        lis.append(x[i] + x[i+1])
        i +=1
    return lis

print(acha_bigramas('batalha'))