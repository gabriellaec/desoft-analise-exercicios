def calcula_aumento(salario):
    salarioF = float(salario)
    if salarioF <= 1250:
        salario_novo = salarioF*1,15
        return salario_novo
    else:
        salario_novo = salarioF*1,1
        return salario_novo