a=int(input('Qual a distancia a ser percorrida? '))
if a<=200:
    b=a*0.50
    return b
else a>200:
    b=100+(a-200)*0.45
    return b
print('O valor a ser pago é {0:.2f}'.format(b))

      

    