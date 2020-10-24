def calcula_valor_devido(valor_emprestado, numero_meses, taxa):
    total = valor_emprestado * (1 + taxa)**numero_meses
    return total