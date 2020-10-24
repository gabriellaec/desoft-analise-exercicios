def calcula_valor_devido(valor,meses,taxa_juros):
    valor_devido = valor*(1+taxa_juros)**meses
    return valor_devido