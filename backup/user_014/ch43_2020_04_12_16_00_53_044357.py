numero_para_nome = {1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6:'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}

numero = int(input('Digite um número: '))

if numero in numero_para_nome:
    print('O mês é {0}'.format(numero_para_nome[numero]))
else:
    print('Esse número não tem um mês correspondente')