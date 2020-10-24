salario = float(input("Qual o seu salário? "))
def calcula_aumento(salario):
    if salario > 1250:
    	print("Aumento para {0}".format(1.1*salario))
    else:
        print("Aumento para {0}".format(1.15*salario))