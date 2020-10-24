def calcula_aumento(float(input(salário))):
	if salário<=1250:
		return("O aumento será de R${0:.2f}".format(salário*1.15))
	else:
		return("O aumento será de R${0:.2f}".format(salário*1.1))