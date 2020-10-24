def tempo(d,h,m,s):
    total=86400*d+3600*h+60*m+s
    return total


dias=int(input("Dias: "))
horas=int(input("Horas: "))
minutos=int(input("Minutos: "))
segundos=int(input("Segundos: "))

print(tempo(dias,horas,minutos,segundos))