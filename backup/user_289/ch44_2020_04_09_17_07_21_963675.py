dicionario_meses = dict()
dicionario_meses = {'JANEIRO': 1, 'FEVEREIRO': 2, 'MARÇO': 3, 'ABRIL': 4, 'MAIO': 5, 'JUNHO': 6, 'JULHO': 7, 'AGOSTO': 8, 'SETEMBRO': 9, 'OUTUBRO': 10, 'NOVEMBRO': 11, 'DEZEMBRO': 12}
mes = input('Qual o nome do mês: ')
if mes in dicionario_meses:
    print('O número do mês é {0}'.format(dicionario_meses[M]))