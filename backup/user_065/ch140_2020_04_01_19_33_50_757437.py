def faixa_notas(notas):
    result = [0,0,0]
    for n in range(len(notas) -1):
        if notas[n] < 5:
            result[0] = result[0] + 1
        if notas[n] >= 5 and notas[n] <= 7:
            result[1] = result[1] + 1
        if notas[n] > 7:
            result[2] = result[2] + 1
    return result