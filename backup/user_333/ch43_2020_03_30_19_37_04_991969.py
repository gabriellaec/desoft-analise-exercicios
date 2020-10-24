def nome_mes(n):
    lista_meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
    mes=lista_meses[n-1]
    return mes

numero_do_mes=int(input('número do mês: '))

print(nome_mes(numero_do_mes))