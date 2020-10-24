def calcula_valor_devido(valor_emprestado,ndemeses,taxa):
    y=valor_emprestado*(1+taxa)**ndemeses
    return y
