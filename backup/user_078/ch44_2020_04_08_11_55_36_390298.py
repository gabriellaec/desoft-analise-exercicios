dict_de_meses={'janeiro': '1', 'fevereiro':'2', 'março': '3', 'abril': '4', 'maio': '5', 'junho': '6', 'julho':'7', 'agosto':'8', 'setembro':'9', 'outubro':'10', 'novembro':'11', 'dezembro':'12'}
nome_do_mes=input('Qual é o mês? ')

if nome_do_mes in dict_de_meses:    
    numero_do_mes = dict_de_meses[nome_do_mes]
    print('Número de {0} é {1}'.format(nome_do_mes, numero_do_mes))