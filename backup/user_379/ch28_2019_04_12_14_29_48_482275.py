a=int(input('digite a sua velocidade'))
if a<=80:
    print('Não foi multado')
else:
    print('você foi multado em'{:.2f}).format((a-80)*5)