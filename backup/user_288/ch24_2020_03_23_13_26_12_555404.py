def calcula_aumento (salario):
    if salario > 1250:
        calcula_aumento = salario + 0,1
    else:
        calcula_aumento = salario + 0,15
    return calcula_aumento
print ('Seu salario atual é {0}'. format (calcula_aumento))