def calcula_segundos(d,h,m,s):
    h=24*d+h
    m=60*h+m
    s=60*m+s

    return s
h=int(input("quantas horas: "))
d=int(input("quantos dias: "))
m=int(input("quantos minutos: "))
s=int(input("quantos segundos: "))
print (calcula_segundos(d,h,m,s))
