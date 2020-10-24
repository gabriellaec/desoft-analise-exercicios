dicionario_meses = {'JANEIRO': 1, 'FEVEREIRO': 2, 'MARÇO': 3, 'ABRIL': 4, 'MAIO': 5, 'JUNHO': 6, 'JULHO': 7, 'AGOSTO': 8, 'SETEMBRO': 9, 'OUTUBRO': 10, 'NOVEMBRO': 11, 'DEZEMBRO': 12}
nome_mes = input('Qual o mês: ')
if nome_mes in dicionario_meses:
    numero_mes = dicionario_meses[nome_mes]
    print('O mês {0} é o {1}.'.format(nome_mes, numero_mes)
