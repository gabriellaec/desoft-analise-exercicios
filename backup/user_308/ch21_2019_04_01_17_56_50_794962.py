def conta(valor)
	valor= float(input("Qual foi o valor da conta?: "))
	valor_com_dez= valor*1.1
    return "Valor da conta com 10%: {0:.2f}".format(valor_com_dez
print conta(valor)