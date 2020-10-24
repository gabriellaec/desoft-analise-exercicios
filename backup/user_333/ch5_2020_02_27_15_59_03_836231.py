# -*- coding: utf-8 -*-
"""
programa que calcula a massa em quilogramas através de um input da massa em libras

@autor: Francisc Janela
"""

#função que multiplica a massa em libras pela constante de conversão em quilogramas
def libras_para_kg(L):
    kg=L*0.453592
    return kg

#input da massa em libras para a conversão
massa_em_libras=50
print('{0} libras equivalem a {1}kg.'.format(massa_em_libras,libras_para_kg(massa_em_libras)))