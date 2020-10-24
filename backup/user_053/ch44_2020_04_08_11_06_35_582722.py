meses_do_ano = {'Janeiro': 1, 'Fevereiro': 2, 'Março': 3, 'Abril': 4, 'Maio': 5, 'Junho': 6, 'Julho': 7, 'Agosto': 8, 'Setembro': 9, 'Outubro': 10, 'Novembro': 11, 'Dezembro': 12}

pergunta = input('Digite o mês do ano: ')

if pergunta in meses_do_ano:
    numero = meses_do_ano[pergunta]
    print('O número do mês é {0}'.format(numero))
else:
    print('Nome não localizado')