
def conta_final(conta):
    y=conta+ 0.1*conta
 	return y

a=float(input(" Qual o valor da conta?"))
print("Valor da conta com 10%: R${0:.2f}".format(conta_final(a)))