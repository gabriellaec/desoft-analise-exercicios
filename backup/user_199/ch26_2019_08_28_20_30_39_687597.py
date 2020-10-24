d=int(input('digite uma quantidade de dias: '))
h=int(input('digite uma quantidade de horas: '))
m=int(input('digite uma quantidade de minutos: '))
s=int(input('digite uma quantidade de segundos: '))

def segundos(d,h,m,s):
    y=(d*24*60*60)+(h*60*60)+(m*60)+s
    return y
print(segundos(d,h,m,s))