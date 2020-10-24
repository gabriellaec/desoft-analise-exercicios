def calcula_aumento(salario):
    if int(salario) > 1250:
        salario = 1.1*salario
        print("Aumento de {0}".format(salario))
    else:
        salario = 1.15*salario
        print("Aumento de {0}".format(salario))