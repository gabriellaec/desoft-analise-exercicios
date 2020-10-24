a=float(input('Qual a distancia a ser percorrida? '))
if a<=200:
    b=a*0.50
else a>200:
    b=100+(a-200)*0.45
print('O valor a ser pago é {0:.2f}'.format(b))

      

    