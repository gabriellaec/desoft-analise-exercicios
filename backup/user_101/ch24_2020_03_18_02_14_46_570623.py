def calcula_aumento(salario):
    salario_maior=salario*1.10
    salari0_menor=salario*1.15
    if salario>1250.00:
        return salario_maior
    else:
        return salario_menor
    