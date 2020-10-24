def calcula_aumento (salario_atual):
    if salario_atual > 1250:
        salario_aumentado = salario_atual * 0.1
    else:
        salario_aumentado = salario_atual * 0.15
    return salario_aumentado
print ('Seu salário é: {0}'.format(salario_aumentado))