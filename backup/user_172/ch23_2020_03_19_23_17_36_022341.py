x = float(input('qual velocidade? ')
if x <= 80:
    print ('Não foi multado')
else:
    print ('{0:.2f}'.format((x-80)*5))