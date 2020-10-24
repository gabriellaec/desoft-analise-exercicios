def calcula_aumento(salario):
    if flat(salario) > 1250:
    	salario = 0.1*salario
        print("Aumento de {0}".format(salario))
    else:
        salario = 0.15*salario
        print("Aumento de {0}".format(salario))