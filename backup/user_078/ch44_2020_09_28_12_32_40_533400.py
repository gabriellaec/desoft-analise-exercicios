dicionario_meses = {
        'Janeiro': 1, 
        'Fevereiro': 2,
        'Março': 3,
        'Abril': 4, 
        'Maio': 5, 
        'Junho': 6, 
        'Julho': 7,
        'Agosto': 8, 
        'Setembro': 9, 
        'Outubro': 10, 
        'Novembro': 11, 
        'Dezembro': 12 
}

nome_mes = str(input('Qual é o nome do mês? '))

numero = dicionario_meses[nome_mes]
print('O número do mês é {0}'.format(numero))