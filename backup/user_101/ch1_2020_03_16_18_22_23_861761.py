def calcula_valor_devido(valor, meses, taxa):
    divida=valor*(1+taxa)**meses
    return divida