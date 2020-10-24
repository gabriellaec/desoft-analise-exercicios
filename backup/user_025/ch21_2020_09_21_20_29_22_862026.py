x = int(input('Diga um valor de dias'))
y = int(input('Diga um valor de horas'))
z = int(input('Diga um valor de minutos'))
c = int(input('Diga um valor de segundos'))

print('O valor total em segundos é {0:.4f}'.format(x*86400 + y*3600 + z*60 + c))
