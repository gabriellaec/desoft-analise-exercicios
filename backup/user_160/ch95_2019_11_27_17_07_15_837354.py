def mais_populoso(dict):
    maior = soma[0][0]
    i = 0
    soma = []
    while i <= len(dict):
        soma [i] = dict[i][i]
    while i <= len(dict):
        if soma[i+1][1] > maior:
            maior = soma[i+1][0]
        else:
            continue
    print(maior)