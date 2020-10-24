q=int(input('quantos cigarros você fuma por dia: '))
t=float(input('há quantos anos você fuma: '))
Y=(q*t*10*365)/1440
print('o tempo de vida perdido em dias é %6.1f' % Y)