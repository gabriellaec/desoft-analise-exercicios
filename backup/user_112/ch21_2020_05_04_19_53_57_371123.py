dias = input('dias')
horas = input ('horas')
minutos = input('minutos')
segundos = input('segundos')

d = int(dias) * 24 * 60 * 60
h = int(horas) * 60 * 60
m = int(minutos) * 60
s = int(segundos)

print(d + h + m + s) 