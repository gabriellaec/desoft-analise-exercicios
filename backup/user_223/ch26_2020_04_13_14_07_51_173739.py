valor_casa = float(input("Insira o valor da casa a ser comprada: "))
salario = float(input("Insira seu salario: "))
anos = int(input("Insira a quantidade de anos em que deseja pagar a casa: "))
meses = anos*12
valor_prestacao = valor_casa/meses
if valor_prestacao > salario*0.3:
	print("Empréstimo não aprovado")
elif 0<valor_prestacao<salario*0.3:
	print("Empréstimo aprovado")