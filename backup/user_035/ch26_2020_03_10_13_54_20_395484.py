valor_da_casa = int(input("Diga o valor da casa: "))
salário = int(input("Diga o seu salário: "))
anos = int(input("Diga a quantidade de anos que quer pagar: "))
meses = anos*12
valor_da_prestação = valor_da_casa/meses
if valor_da_prestação>(0.3*salário):
	print("Empréstimo não aprovado")
else:
	print("Empréstimo aprovado")