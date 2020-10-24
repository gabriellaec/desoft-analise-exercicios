def  calcula_valor_devido(valor_emprestado,meses,taxa_de_juros):
    M = valor_emprestado*(taxa_de_juros+1)**meses
    return M