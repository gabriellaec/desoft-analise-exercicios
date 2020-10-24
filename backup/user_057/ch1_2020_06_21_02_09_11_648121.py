def calcula_valor_devido(valor, meses, taxa):
    if meses == 0:
        return valor
    else:
        while i <= len(meses):
            valor = valor*taxa
            i += 1
    return valor    