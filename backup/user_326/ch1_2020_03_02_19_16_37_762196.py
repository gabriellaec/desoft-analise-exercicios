""" 
Calculo Juros Compostos

Autor: Bernardo C. Capoferri 
"""

def calcula_valor_devido(numero_meses):
    valor_emprestado = 1000   #insira valor emprestado inicialmete
    taxa_de_juros = 0.1       #insira taxa de juros mensal
    formula_jurosc = valor_emprestado*(1+taxa_de_juros)**numero_meses
    return formula_jurosc

meses = 1
deficit= calcula_valor_devido(meses)
print (deficit)
    