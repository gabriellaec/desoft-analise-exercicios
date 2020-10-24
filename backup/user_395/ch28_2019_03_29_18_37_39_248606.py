x = float(input('Qual a sua velocidade em Km/h?'))
if x > 80:
    m = (x-80)*5
    print('{0:.2f}'.format(m))
else:
    print('Não foi multado')