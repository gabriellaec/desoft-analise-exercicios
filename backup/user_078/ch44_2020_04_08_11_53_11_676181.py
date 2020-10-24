dict_de_meses={'Janeiro': '1', 'Fevereiro':'2', 'Março': '3', 'Abril': '4', 'Maio': '5', 'Junho': '6', 'Julho':'7', 'Agosto':'8', 'Setembro':'9', 'Outubro':'10', 'Novembro':'11', 'Dezembro':'12'}
nome_do_mes=input('Qual é o mês? ')

if nome_do_mes in dict_de_meses:    
    numero_do_mes = dict_de_meses[nome_do_mes]
    print('Número de {0} é {1}'.format(nome_do_mes, numero_do_mes))