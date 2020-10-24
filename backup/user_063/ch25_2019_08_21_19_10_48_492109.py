x = int(input('Distancia Percorrida: '))
if x<=200:
    a = x*0.5
if x>=200:
    a = (x-200)*0.45+100
print ('Valor da passsagem:R$ {0:.2f}'.format(a))