"""
Exercício 1: Juros Compostos

Escreva uma função que calcula o valor devido ao final de um empréstimo.
Os argumentos de entrada da função serão: valor emprestado, número de meses e taxa de juros. 
Atenção: usar juros compostos para calcular o valor devido.

@autor: Marcos Vinícius da Silva
Engenharia Mecatrônica - 1ºSemestre - Turma 1B
"""

print('------------------------------------------------------')
print('Digite o valor do empréstimo: ')
a = float(input())

print('------------------------------------------------------')
print('Digite o número de meses desde o empréstimo: ')
b = int(input())

print('------------------------------------------------------')
print('Digite o valor da taxa de juros: ')
c = float(input())

#Definindo a função dos juros compostos.
def calcula_valor_devido(valor_emprestimo, num_meses, valor_taxa_juros):
    valor_devido = (valor_emprestimo*((1 + valor_taxa_juros)**(num_meses)))
    return valor_devido

print('------------------------------------------------------')
print('O valor a ser pago: {}' .format(calcula_valor_devido(a, b, c)))