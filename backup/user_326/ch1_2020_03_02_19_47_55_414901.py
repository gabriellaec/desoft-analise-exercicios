""" 
Calculo Juros Compostos

Autor: Bernardo C. Capoferri 
"""

def calcula_valor_devido(valor_emprestado, numero_meses, taxa_de_juros):
    formula_jurosc = valor_emprestado*(1+taxa_de_juros)**numero_meses
    return formula_jurosc


    