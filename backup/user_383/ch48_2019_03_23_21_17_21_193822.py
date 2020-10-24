lista_mes=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
mes=str(input('Qual o mês que você deseja saber o número correspondente? :'))
while mes < len(lista_mes) and mes >=1 and mes <= 12:
	print(lista_mes[mes-1])

    