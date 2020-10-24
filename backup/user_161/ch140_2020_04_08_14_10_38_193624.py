def faixa_notas(notas):
    faixas = [0, 0, 0]
    for nota in notas:
        if nota < 5:
            faixas[0] += 1
        elif nota >=5 and nota <=7:
            faixas[1] += 1
        else:
            faixas[2] += 1
    return faixas        