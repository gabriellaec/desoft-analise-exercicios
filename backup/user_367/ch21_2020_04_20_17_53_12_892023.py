y=float(input('Dias: '))
x=float(input('horas: '))
p=float(input('minutos: '))
o=float(input('segundos: '))

soma= (y* 86400) + (x * 3600) + (p*60) + o
print('soma é {0}' .format(soma))