#Pergunta os dias, horas, minutos e segundos
def soma(x,y,z,w):
    c = x + y + z + w
    return c

d = int(input('Quantos dias? '))*86400
h = int(input('Quantas horas? '))*3600
m = int(input('Quantos minutos? '))*60
s = int(input('Quantos segundos? '))

t = soma(d,h,m,s)
print(t)





