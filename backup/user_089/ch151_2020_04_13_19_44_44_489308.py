def classifica_lista(x):
    if x == [] or len(x) <= 2:
        return "nenhum"
    i = 0
    while i < len(x):
        if x[i] > x[i+1]:
            return "decrescente"
        if x[i] < x[i+1]:
            return "crescente"