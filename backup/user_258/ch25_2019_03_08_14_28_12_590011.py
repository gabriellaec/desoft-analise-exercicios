a=int(input('Qual a distancia a ser percorrida? '))
if a<=200:
    b=a*0.50
    return b
else a>200:
    c=100+(a-200)*0.45
    return c
print('O valor a ser pago é {0:.2f}'.format(b or c))

      

    