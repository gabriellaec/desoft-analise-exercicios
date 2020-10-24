def verifica_numero(x):
    X = list(map(int, str(x)))
    N = True
    soma = 0
    for e in X:
        soma += e**e
    if soma == x:
        N= True
    else:
        N=False
    return N
    