def calcula_valor_devido(valor,meses,taxa_juros):
    #taxa_nova = taxa_juros/100
    valor_devido = valor*(1+taxa_juros)**meses
    return valor_devido