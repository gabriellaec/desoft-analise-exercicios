def calcula_valor_devido(valor_emprestado, taxa, meses)
    y = valor_emprestado*(1+taxa)**meses
    return y