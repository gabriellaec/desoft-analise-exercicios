

def calcula_valor_devido(valor_emprestado,numero_de_meses,taxa_de_juros):
    montante = valor_emprestado * (1 + taxa_de_juros / 100) ** numero_de_meses
    
    return montante
