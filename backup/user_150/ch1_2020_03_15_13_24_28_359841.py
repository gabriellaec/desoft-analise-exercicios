def calcula_valor_devido(valor_emprestado,meses,taxa_de_juros):
    montante = valor_emprestado*(1+taxa_de_juros)**meses
    return montante