def faixa_notas(x):
    x = list
    i = 0
    notas = list
    soma1 = 0
    soma2 = 0
    soma3 = 0
    while i <= len(x):
        if x[i] < 5:
            soma1 = soma1 + 1
        if x[i] 5 <= x <= 7:
            soma2 = soma2 + 1
        if x[i] > 7:
            soma3 = soma3 + 1
    Lista = [soma1,soma2,soma3]
    return Lista