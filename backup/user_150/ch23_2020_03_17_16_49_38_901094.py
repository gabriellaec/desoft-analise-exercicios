forma = float(input('Qual a sua velocidade? '))
if forma > 80:
    m = 5 * (forma - 80)
    print('Você foi multado em:', m)
else:
    print('Não foi multado')