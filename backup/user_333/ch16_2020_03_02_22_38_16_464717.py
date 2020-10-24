# -*- coding: utf-8 -*-
"""
programa para calcular o valor da conta final com a adição de 10%

@author: Francisco Janela
"""
#input do usuário
valor=input('valor da conta: ')

#calcula com os 10% e produz um resultado com 2 casas decimais
print('Valor da conta com 10%: R$ {0:.2f}'.format(float(valor)*1.1))