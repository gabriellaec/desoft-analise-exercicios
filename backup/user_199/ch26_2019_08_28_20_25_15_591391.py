d=int(input('digite uma quantidade de dias: '))
h=int(input('digite uma quantidade de horas: '))
m=int(input('digite uma quantidade de minutos: '))

def segundos(d,h,m):
    s=(d/24*60*60)+(h/60*60)+(m/60)
    return s
print(segundos(d,h,m))