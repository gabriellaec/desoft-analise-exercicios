vel=int(input('Qual a velocidade? '))
def multa(vel):
    if vel>80:
        print('multa de {0.:2f}'.format((vel-80)*5)
    else:
        print('Não foi multado')