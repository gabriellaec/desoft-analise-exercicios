def soma(x, y, z, o):
    w = x + y + z + o
    return w
    
a =int(input('Quantos dias?'))*24*60*60
b =int(input ('Quantas horas?'))*60*60
c =int(input ('Quantos minutos?'))*60
d =int(input ('Quantos segundos?'))

e = soma(a,b,c,d)

print(e)