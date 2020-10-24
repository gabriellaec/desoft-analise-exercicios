a = int(input('Quantos cigarros você fuma por dia?'))
b = int(input('Há quantos anos você fuma?'))
c = a * 10 * ( b * 365 * 24 * 60)
d = c / 60 * 24
print ('Você já perdeu {0} dias de vida' .format(d))