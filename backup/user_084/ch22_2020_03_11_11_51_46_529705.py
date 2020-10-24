q=int(input('quantos cigarros voce fuma por dia: '))
t=float(input('há qauntos anos você fuma: '))
Y=(q*t*10*365)/1440
print('o tempo de vida perdido em dias é %6.1f' % Y)