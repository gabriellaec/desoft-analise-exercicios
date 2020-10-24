p = float(input('velocidade:'))
if p>80:
    m = (p - 80) * 5
    print('valor multa: {:.2f}'.format(m))
    
else:
    print ('não foi multado')