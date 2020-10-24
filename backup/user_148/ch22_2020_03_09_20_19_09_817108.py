c = float(input('Quantos cigarros você fuma por dia? '))
a = float(input('Há quantos anos você fuma? '))
t = c*a*365
p = (c*a*3650)/1440
print('Sinto informar que você tem menos {} dias de vida!!'.format(p))