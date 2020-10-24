def calcula_valor_devido (valor, meses, taxa):
    montante = valor * (1+taxa)**meses
    return montante