e = float ( input ("escreva o valor que deseja ser emprestado, em reais: "))
n = float( input ("escreva o número de meses que o dinheiro ficará emprestado: "))
j = float ( input ("escreva o valor do juros, em porcentagem: "))


def calcula_valor_devido(e,j,n):  
    c = round( e * ( 1 + j/100) ** n, 2)
    return c

print ('O valor a ser devolvido é {0} reais.'.format(calcula_valor_devido(e,j,n)) )

