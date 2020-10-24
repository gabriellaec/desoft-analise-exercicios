valor_casa=float(input("Qual o valor da compra? ")
salario=float(input("Qual o seu salario? ") 
meses_a_pagar=int(input("Quantas prestações? ")
if valor_casa/meses_a_pagar>0.3*salario:
	print ("Empréstimo não aprovado")
else:
	print ("Empréstimo aprovado")                   