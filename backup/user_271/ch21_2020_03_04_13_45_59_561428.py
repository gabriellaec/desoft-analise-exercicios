d=input('Quantos dias? ')
h=input('Quantas horas? ')
m=input('Quantos minutos? ')
s=input('Quantos segundos? ')
h=int(h)
m=int(m)
d=int(d)
s=int(s)
sh=3600*h
ds=86400*d
sm=60*m
total=sh+sm+s+ds
print(total)
