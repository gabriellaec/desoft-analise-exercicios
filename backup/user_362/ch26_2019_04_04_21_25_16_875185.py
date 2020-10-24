def total_segundos(s,m,h,d):
    s=1*s
    m =60*s
    h=60*m
    d=24*h
    soma = m+h+d+s
    return soma

d=int(input("digite qtos dias: "))
h=int(input("digite qtas horas: "))
m=int(input("digite qtos minutos: "))
s=int(input("digite qtos segundos: "))
print (total_segundos(s,m,h,d))