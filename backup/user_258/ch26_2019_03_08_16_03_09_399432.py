def soma(s,m,h,d):
    q=s+86400*d+3600*h+60*m
    return q
d=int(input('Qual a quantidade de dias: '))
h=int(input('Qual a quantidade de horas: '))
m=int(input('Qual a quantidade de minutos: '))
s=int(input('Qual a quantidade de segundos: '))
print(soma(s,m,h,d))

