def calcula_valor_devido(capital, meses, taxa):
    montante = capital * (1 + taxa)**meses
    return montante