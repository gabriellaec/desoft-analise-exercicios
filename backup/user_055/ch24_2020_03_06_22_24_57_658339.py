def calcula_aumento(salario):
    salario = int(input('Quanto você ganha por mês?: '))
    if salario > 1250:
        aumento = salario*0.1
    if salario <= 1250:
        aumento  = salario*0.15