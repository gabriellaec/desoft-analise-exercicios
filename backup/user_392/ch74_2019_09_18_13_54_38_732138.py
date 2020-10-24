def conta_bigramas(x):
    dic_notas = {}
    i = 0
    while i < len(x)-1:
        bigrama = x[i]+x[i+1]
        print(bigrama)
        if bigrama in dic_notas:
            dic_notas[bigrama] += 1
        else:
            dic_notas[bigrama] = 1
    
        i+=1
    return dic_notas