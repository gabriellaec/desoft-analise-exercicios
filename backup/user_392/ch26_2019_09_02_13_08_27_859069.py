d = float(input('digite o total de dias:'))
h = float(input('digite o total de horas:'))
m = float(input('digite o total de minutos))
s = float(input('digite o total de segundos:'))

total_d = d*86400
total_h = h*3600
total_m = m*60
total_s = s

total = total_s + total_h + total_d + total_m

print(total)
