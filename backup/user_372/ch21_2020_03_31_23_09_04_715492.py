a=int(input('Quantos dias? '))
b=int(input('Quantos horas? '))
c=int(input('Quantos minutos? '))
segundos=int(input('Quantos segundos? '))
a=86400*a
b=3600*b
c=60*c
d=a+b+c+segundos
print(d)
