Meses = {'janeiro': '1', 'fevereiro': '2', 'março': '3', 'abril': '4', 'maio': '5', 'junho': '6', 'julho': '7', 'agosto': '8', 'setembro': '9', 'outubro': '10', 'novembro': '11', 'dezembro': '12'}
m = input('Qual o nome do mês?')
if m in Meses:
    Numero = Meses[m]
    print('{0} em número é {1}'.format(m, Numero))
    else:
    print('A palavra {0} não é um mês'.format(m))