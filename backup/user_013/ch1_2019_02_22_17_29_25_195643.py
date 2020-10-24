"""

Exercício Desafio: fazer um código que receba o valor de empréstimo, taxa de 
juros e número de meses que o dinheiro ficará emprestado. O montante será "cal-
cula o valor devido". Seja 

empréstimo = e
taxa de juros = j
número de meses = n
montante = calcula_valor_devido
calcula_o_valor_devido = c

"""

e = float ( input ("escreva o valor que deseja ser emprestado, em reais: "))
j = float ( input ("escreva o valor do juros, em porcentagem: "))
n = float( input ("escreva o número de meses que o dinheiro ficará emprestado: "))

def calcula_valor_devido(e,j,n):  
    c = round( e * ( 1 + j/100) ** n, 2)
    return c

print ('O valor a ser devolvido é {0} reais.'.format(calcula_valor_devido(e,j,n)) )

