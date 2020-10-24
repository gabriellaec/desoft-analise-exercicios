# -*- coding: utf-8 -*-
"""
programa que calcula a redução da expectativa de vida para os fumantes

@author: Francisco Janela
"""

#calcula a redução em dias
def reducao_tempo_de_vida(cigarros,anos):
    por_ano=cigarros*365*10
    perda_minutos=10*por_ano*anos
    perda_dias=perda_minutos/1440
    return perda_dias

#input do usuário sobre seus hábitos
cigarros_por_dia=input('Quantos cigarros fuma por dia? ')
anos_fumando=input('Faz quantos anos que fuma? ')

#imprime o valor de dias inteiros
print('sua vida foi reduzida com sucesso em {0} dias'.format(reducao_tempo_de_vida(int(cigarros_por_dia),int(anos_fumando))))