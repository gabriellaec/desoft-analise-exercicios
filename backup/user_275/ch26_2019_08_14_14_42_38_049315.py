def quantidade_segundos(a,b,c,d):
 return a*86400+b*3600+c*60+d

a=int(input("digite o numero de dias:"))
b=int(input("digite o numero de horas:"))
c=int(input("digite o numero de minutos:"))
d=int(input("digite o numero de horas:"))
e=(quantidade_segundos(a,b,c,d))
print(e)