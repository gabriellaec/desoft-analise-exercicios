def calcula_aumento(salario):
    if salario > 1250:
        salarioF = salario + (salario*0.1)
    elif salario<= 1250:
        salarioF = salario + (salario*0.15)
    return salarioF