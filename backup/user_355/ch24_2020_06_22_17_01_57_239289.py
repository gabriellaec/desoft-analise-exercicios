def calcula_aumento (salario):
    if (salario < 1250.00 or salario == 1250.00):
        x=salario*1.15
    else :
        x=salario*1.1
    return x
