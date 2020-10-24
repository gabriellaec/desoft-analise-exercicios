def em_segundos(d,h,m,s):
    y = d*86400 + h*3600 + m*60 + s
    return y

d = int(input("Quantos dias? "))
h = int(input("Quantas horas? "))
m = int(input("Quantos minutos?"))
s = int(input("Quantos segundos? "))
resultado = em_segundos(d,h,m,s)

print(resultado)