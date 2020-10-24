def calcula_valor_devido(valor, meses, taxa):
    parcela= valor/meses
    valor_final= parcela*taxa
    return valor_final