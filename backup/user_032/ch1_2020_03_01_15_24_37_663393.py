"""
Calcula o valor devido ao final de um empréstimo de 10000 reais com uma taxa de juros compostas de 3% ao mês.
@author: Natália Carreras
"""

# Função do valor devido ao final de um empréstimo
def calcula_valor_devido(numero_meses):
    valor_devido=10000+1.03**numero_meses
    return valor_devido

#Qual o valor após 18 meses?
meses=18
valor=calcula_valor_devido(meses)
print(valor)