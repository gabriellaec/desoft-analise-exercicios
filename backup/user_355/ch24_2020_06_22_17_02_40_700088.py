def calcula_aumento (salario):
    if (salario < 1250.00 or salario == 1250.00):
        x=salario*0.15
    else :
        x=salario*0.1
    return x
