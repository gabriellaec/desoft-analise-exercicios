def calcula_aumento(salario):
    if salario > 1250:
        salarioF = salario + (salario*0.1)
    else:
        salarioF = salario + (salario*0.15)
    return salarioF