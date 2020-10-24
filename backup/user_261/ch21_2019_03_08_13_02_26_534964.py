conta=float(input(" Qual o valor da conta?"))
def conta_final(conta):
    y=conta+ 0.1*conta
 	return("Valor da conta com 10%: R${0:.2f}".format(y))