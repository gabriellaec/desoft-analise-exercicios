def calcula_valor_devido ( valor, taxa, meses):
    m= valor*(1+taxa/100)**meses
    return m
