i=0
lista_mes=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
mes=str(input('Qual o mês que você deseja saber o número correspondente? :'))
while mes < len(lista_mes) and mes >= 1 and mes <= 12:
    if mes == lista_mes[i]:
        print(i+1)