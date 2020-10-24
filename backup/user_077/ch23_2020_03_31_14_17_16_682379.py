a=float(input('Velocidade'))
b=5*(a-80)
if a>80:
    print('Você foi multado no valor de R${0:.2f}'.format(b))
else:
    print ('Não foi multado')