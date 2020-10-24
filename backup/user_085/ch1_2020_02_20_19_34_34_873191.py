def calcula_valor_devido(x):
    y = 10000 * (1 + 0.10) ** x
    return y
print(calcula_valor_devido(0))
'''x é o nº de meses após o emprestimo e y é o valor total pago'''
'''assume-se que o valor de empréstimo é 10000 UM e que a taxa de pagamento é de 10 % '''