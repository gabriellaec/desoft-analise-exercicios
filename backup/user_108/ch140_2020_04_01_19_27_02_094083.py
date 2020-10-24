def faixa_notas(notas):
    quant_notas = [0,0,0]
    for nota in notas:
        if nota < 5:
            quant_notas[0] += 1
        elif nota > 7:
            quant_notas[2] += 1
        else:
            quant_notas[1] += 1 
    return quant_notas