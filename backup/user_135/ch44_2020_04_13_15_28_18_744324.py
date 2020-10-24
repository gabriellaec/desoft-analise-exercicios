# Criando um dicionário

dic_mes_numero = {}
meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
numeros = list(range(1,13))

for indice in range (12):
    dic_mes_numero[meses[indice]] = numeros[indice]

# Execução

mes = input('Mês: ')

if mes in dic_mes_numero:
    print('O número correspondente a {} é igual a {}.'.format(mes, dic_mes_numero[mes]))
else:
    print('Não existe nenhum mês com esse nome. Veja se você não escreveu errado ou colocou alguma letra maiúscula.')