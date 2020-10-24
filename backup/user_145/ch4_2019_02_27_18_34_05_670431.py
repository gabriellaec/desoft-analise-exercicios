# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:21:03 2019
@author: celsohad
Escreva uma função que recebe um número inteiro representando a idade de uma pessoa e devolve uma string conforme a seguinte regra:
"crianca" se a pessoa tem até 11 anos, inclusive; "adolescente" se a pessoa tem entre 12 e 17 anos, inclusive;
"adulto" se a pessoa tem 18 anos ou mais. Observação: note que "crianca" deve ser com "c" e não "ç".
"""

def classifica_idade(x):
	if x <= 11:
		return 'Crianca'
	if 12<=x<=17:
		return 'Adolecente'
	if x>=18:
		return 'Adulto'
print(idade(10))
print(idade(12))
print(idade(21))