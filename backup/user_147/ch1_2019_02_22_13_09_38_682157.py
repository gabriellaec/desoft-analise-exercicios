def calcula_valor_devido(valor, meses, taxa):
    valor_devido = valor * taxa ** meses
    return valor_devido
