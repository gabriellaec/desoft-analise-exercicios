numero_meses = {'janeiro': '1', 'fevereiro': '2', 'março': '3', 'abril': '4', 'maio': '5', 'junho': '6', 'julho': '7', 'agosto': '8', 'setembro': '9', 'outubro': '10', 'novembro': '11', 'dezembro': '12'}

mes_escolhido = input("Qual o é o mês? ")

if mes_escolhido in numero_meses:
    numero = numero_meses[mes_escolhido]
    print('O número do mês é {}'.format(numero))
else:
    print('esse mês {} não existe na lista.'.format(mes_escolhido))