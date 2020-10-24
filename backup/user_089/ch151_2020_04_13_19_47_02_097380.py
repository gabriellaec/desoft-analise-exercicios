def classifica_lista(x):
    if x == [] or len(x) <= 2:
        return "nenhum"
    e = 0
    while e < len(x):
        if x[e] > x[e+1] and x[e] < x[e+1]:
            e += 1
            return "nenhum"
   
    i = 0
    while i < len(x):
        if x[i] > x[i+1]:
            i += 1
            return "decrescente"
        if x[i] < x[i+1]:
            i += 1
            return "crescente"