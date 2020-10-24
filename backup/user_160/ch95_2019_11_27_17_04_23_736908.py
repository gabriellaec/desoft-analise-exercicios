def mais_populoso(dict):
    maior = dict[0][0]
    i = 0
    while i <= len(dict):
        if dict [i+1][1] > maior:
            maior = dict [i+1][0]
        else:
            continue
    print(maior)