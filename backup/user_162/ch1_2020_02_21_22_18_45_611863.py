def calcula_valor_devido(valor_emprestado, número_de_meses, taxa_de_juros):
    montante = valor_emprestado*(1 + (taxa_de_juros/100))**número_de_meses
    return(montante)
