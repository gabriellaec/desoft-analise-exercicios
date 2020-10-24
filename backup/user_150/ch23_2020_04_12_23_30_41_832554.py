forma = float(input('Qual a sua velocidade? '))
if forma > 80:
    m = 5.00 * (forma - 80)
    print('Você foi multado em: {0:.2f}'.format(m))
else:
    print('Não foi multado')