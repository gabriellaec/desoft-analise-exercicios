def total(a,b,c,d):
    dias = 24*3600*a
    horas = 3600*b
    minutos = 60*c
    segundos = d
    t = dias+horas+minutos+segundos

    return t

d = int(input('Insira a quantidade de dias: '))
h = int(input('Insira a quantidade de horas: '))
m = int(input('Insira a quantidade de minutos: '))
s = int(input('Insira a quantidade de segundos: '))

print (total(d,h,m,s))
