def calcula_aumento(salario):
    if float(salario) > 1250:
    	print("Aumento de {0}".format(0.1*salario))
    else:
        print("Aumento de {0}".format(0.15*salario))