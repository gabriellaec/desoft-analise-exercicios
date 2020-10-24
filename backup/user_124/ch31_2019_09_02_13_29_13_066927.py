valor_casa = int(input("insira o valor da casa: ")
salario = int(input("insira o seu salario: ")
anos = int(input("em quantos anos ira passar: ")

prestacao = valor_casa * (anos / 12)

if prestacao > salario * 0.3:
	print("Empréstimo não aprovado")
else:
	print("Empréstimo aprovado")