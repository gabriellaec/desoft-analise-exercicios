nome_do_mes = input('Qual o mes?')
lista_com_nome_dos_meses = ['mes_0','janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
lista_numero_do_mes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 0
while i < 13 :
    if nome_do_mes == lista_com_nome_dos_meses[i] :
        print(lista_numero_do_mes[i])
        i += 1