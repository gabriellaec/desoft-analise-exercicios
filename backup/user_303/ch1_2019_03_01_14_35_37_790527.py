def calcula_valor_devido(valor_emprestado, meses, taxa):
    y=valor_emprestado*(1+taxa)**meses
    return y