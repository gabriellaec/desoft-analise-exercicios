i=0
lista_mes=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
mes=str(input('Qual o mês que você deseja saber o número correspondente? :'))
while i < len(lista_mes) and mes in lista_mes:
    if mes == lista_mes[i]:
        print(i+1)
    i+=1