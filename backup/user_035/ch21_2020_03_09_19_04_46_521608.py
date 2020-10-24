d = int(input("Diga uma quantidade de dias: "))
h = int(input("Diga uma quantidade de horas: "))
m = int(input("Diga uma quantidade de minutos: "))
s = int(input("Diga uma quantidade de segundos: "))
Horário = s+(m*60)+(h*3600)+(d*86400)
print Horário