def calcula_aumento(salario):
    if salario > 1250:
        salario += salario*0.10
        return salario
    else:
        salario += salario*0.15
        return salario
       