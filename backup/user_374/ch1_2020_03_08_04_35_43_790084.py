def calcula_valor_devido(valor_emprestado,n_meses,taxa):
    calculo1 = valor_emprestado*(1+taxa)**n_meses
    return(calculo1)