def calcula_aumento(salario):
    salario = input()
    if salario > 1250:
        aumento = salario*0.1
    if salario <= 1250:
        aumento  = salario*0.15