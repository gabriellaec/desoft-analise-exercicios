x = float(input('Qual a sua velocidade em Km/h?'))
if x > 80:
    m = (x-80)*5
    print(m)
    print ('Você foi multado em {0} reais'.format(m))
else:
    print('Não foi multado')