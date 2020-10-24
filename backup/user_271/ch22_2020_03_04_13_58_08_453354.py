c=input('Quantos cigarros você fuma por dia? ')
c=int(c)
a=input('Há quantos anos você fuma?' )
a=int(a)
dias_fumando=a*365
minutos_roubados=c*10*dias_fumando
dias_roubados=minutos_roubados*1440
print(minutos_roubados)
