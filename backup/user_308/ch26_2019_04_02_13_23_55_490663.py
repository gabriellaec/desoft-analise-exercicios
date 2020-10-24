d=float(input("Número de dias: "))
h=float(input("Número de horas: "))
m=float(input("Número de minutos: "))
s=float(input("Número de segundos: "))
total_segundos= (d*24*60*60) + (h*60*60) + (m*60) + s
return total_segundos