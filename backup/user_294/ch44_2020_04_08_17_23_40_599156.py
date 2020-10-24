#i=0
#a=input('digite um mes')
#nome_do_mes=['janeiro','fevereiro','marco','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
#numero_do_mes=['1','2','3','4','5','6','7','8','9','10','11','12']
#nome_do_mes[i]=numero_do_mes[i]
#for a in nome_do_mes:
#    i+=1
#    print(numero_do_mes)

mes_e_numero = {'1': 'janeiro', '2': 'fevereiro', '3': 'marco','4':'abril','5':'maio','6':'junho','7':'julho','8':'agosto','9':'setembro','10':'outubro','11':'novembro','12':'dezembro'}
nome=input('fale o nome do mes: ')
if nome in mes_e_numero:
numero = mes_e_numero[nome]
print('{0} em numero é {1}'.format(nome, numero))
else:
print('o mes {0} não existe no dicionário'.format(nome))