def calcula_aumento (salario):
    if salario > 1250:
       aumento = 0.1*salario
       return aumento
    elif 1250 >= salario:
       aumento = 0.15*salario
       return aumento