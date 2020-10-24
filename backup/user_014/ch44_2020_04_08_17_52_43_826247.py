mes_para_ano = {'janeiro': '1', 'fevereiro': '2', 'março': '3', 'abril': '4', 'maio': '5', 'junho': '6', 'julho':'7', 'agosto': '8', 'setembro': '9', 'outubro': '10', 'novembro': '11', 'dezembro': '12'
                
nome_do_mes = input('Qual é o mês? ')

if nome_do_mes in mes_para_ano:
   print('O mês é {0}'.format(mes_para_ano[nome_do_mes]))