# -*- coding:juros compostos -*-
"""
O programa é utilizado para calcular o valor devido de um empréstimo em juros compostos

@autor: Francisco Janela
"""
#função para calcular o valor devido após um emprestimo a juros compostos
#montante: valor do empréstimo em reais
#meses: número de meses que serão aplicados a taxa de juros
#taxa: taxa de juros mensal aplicada
def calcula_valor_devido(montante,meses,taxa): #parâmetros utilizados para o calculo
    valor_devido=montante*(1+taxa)**meses      #fórmula para calcular o valor devido
    return valor_devido

#escrever o resultado perante os parâmetros estabelecidos na ordem
print('o montante devido é {0}.'.format(calcula_valor_devido(1000,24,0.05))) 