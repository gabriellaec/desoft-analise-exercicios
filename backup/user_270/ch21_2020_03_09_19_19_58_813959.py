a = int(input("Me diga quantos dias: "))
b = int(input("Me diga quantas horas: "))
c = int(input("Me diga quantos minutos: "))
d = int(input("Me diga quantos segundos: "))
total = d + c*60 + b*3600 + 24*3600*a
print(total)