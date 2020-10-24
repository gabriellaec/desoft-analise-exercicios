def calcula_segundos(d,h,m,s):
    y=d*86400+h*3600+m*60+s
    return y
d=int(input('dias? '))
h=int(input("horas? "))
m=int(input('minutos? '))
s=int(input("segundos? "))
p=calcula_segundos(d,h,m,s)
print(p)