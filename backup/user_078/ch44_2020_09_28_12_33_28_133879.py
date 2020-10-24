dicionario_meses = {
        'janeiro': 1, 
        'fevereiro': 2,
        'março': 3,
        'abril': 4, 
        'maio': 5, 
        'junho': 6, 
        'julho': 7,
        'agosto': 8, 
        'setembro': 9, 
        'outubro': 10, 
        'novembro': 11, 
        'dezembro': 12 
}

nome_mes = str(input('Qual é o nome do mês? '))

numero = dicionario_meses[nome_mes]
print('O número do mês é {0}'.format(numero))