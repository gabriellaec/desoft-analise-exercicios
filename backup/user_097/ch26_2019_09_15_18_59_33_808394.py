def totalSegundos(d, h, m, s):
    segundos = ((d*24*60*60) + (h*60*60) + (m*60) + s)
    return segundos

d = float (input("Dias: "))
h = float(input("Horas: "))
m = float(input("Minutos: "))
s = float(input("Segundos: "))

print("O total de segundos é de {0} segundos".format(totalSegundos(d, h, m, s)))