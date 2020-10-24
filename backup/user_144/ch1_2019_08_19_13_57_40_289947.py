def calcula_valor_devido(emprestado,meses,taxa):
    y = emprestado * (1+taxa)**meses
    return y