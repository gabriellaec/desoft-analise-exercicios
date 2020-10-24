vel = int(input())
if v <= 80:
    print('Não foi multado')
else:
    print('{0:.2f}'.format(5*(vel-80)))