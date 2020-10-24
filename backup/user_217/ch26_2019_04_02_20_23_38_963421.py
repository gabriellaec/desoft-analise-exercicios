a=int(input('Quantidade de dias?:'))
b=int(input('Quantidade de horas?: '))
c=int(input('Quantidade de minutos?: '))
d=int(input('Quantidade de segundos?: '))

if a > 0:
    x= a * 86400
if b > 0:
    y = b * 3600
if c > 0:
    z = c * 60
if d > 0:
    w= d * 1
    
print(x+y+z+w)