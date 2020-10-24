def calcula_valor_devido(valor_emprestado, meses, juros):
    devido = valor_emprestado*(1 + (juros/100))**meses 
    return devido
    