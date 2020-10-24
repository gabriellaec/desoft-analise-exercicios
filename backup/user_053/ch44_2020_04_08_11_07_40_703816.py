meses_do_ano = {'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12}

pergunta = input('Digite o mês do ano: ')

if pergunta in meses_do_ano:
    numero = meses_do_ano[pergunta]
    print('O número do mês é {0}'.format(numero))
else:
    print('Nome não localizado')