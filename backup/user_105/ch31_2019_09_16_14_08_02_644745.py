valor_da_casa = float(input('qual o preco da sua casa: '))
salario = float(input('qual o seu salario'))
quantidade_de_prestaçoes = int(input('quantas prestaçoes: '))
valor_mensalidade = valor_da_casa / (quantidade_de_prestaçoes)
if valor_mensalidade > (0.3 * salario):
	print ('Empréstimo não aprovado')
elif valor_mensalidade <= (0.3*salario):
    print ('Empréstimo aprovado')