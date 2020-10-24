def calcula_valor_devido(valor, meses, taxa):
    for i in len(meses):
        valor = valor*taxa
    return valor    