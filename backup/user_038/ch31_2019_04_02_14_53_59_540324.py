valor_casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe seu salario: "))
tempo = int(input("Quantos anos deseja: "))
prestacao = valor_casa/(tempo*12)
if salario>0.3*prestacao:
	print("Empréstimo não aprovado")
else:
	print("Empréstimo aprovado")