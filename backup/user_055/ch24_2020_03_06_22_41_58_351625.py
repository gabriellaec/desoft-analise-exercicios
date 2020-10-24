def calcula_aumento(salario):
    if salario > 1250:
        aumento = salario*0.1
    else:
        if salario <= 1250:
            aumento = salario*0.15