def calcula_aumento(salario):
    salario_maior=salario*0.10
    salario_menor=salario*0.15
    if salario>1250.00:
        return salario_maior
    else:
        return salario_menor
    