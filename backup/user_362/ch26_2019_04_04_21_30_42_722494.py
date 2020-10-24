def total_segundos(s,m,h,d):
    resultado=d*24*60*60+h*3600+m*60+s
    return resultado

d=int(input("digite qtos dias: "))
h=int(input("digite qtas horas: "))
m=int(input("digite qtos minutos: "))
s=int(input("digite qtos segundos: "))
print (total_segundos(s,m,h,d))