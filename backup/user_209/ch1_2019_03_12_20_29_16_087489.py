def calcula_valor_devido (valor_emprestado,meses,juros):
    montante = valor_emprestado * (1 + juros)**meses
    return montante

    
