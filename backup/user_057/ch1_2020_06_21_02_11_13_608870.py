def calcula_valor_devido(valor, meses, taxa):
    if meses == 0:
        return valor
    else:
        M = valor*(1+taxa)**meses
    return M   