#Pergunta os dias, horas, minutos e segundos
def soma(x,y,z,w):
    c = x + y + z + w
    return c

d = input('Quantos dias? ')*86400
h = input('Quantas horas? ')*3600
m = input('Quantos minutos? ')*60
s = input('Quantos segundos? ')

t = soma(d,h,m,s)
print(t)





