a = int(input('Quantos cigarros voce fuma por dia ? '))
b = int(input('A quanto tempo você fuma ?'))

total = (b*365)*a
perdido = (total*10)/24

print('dias perdidos %d' %perdido)