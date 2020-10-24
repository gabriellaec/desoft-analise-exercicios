def totalSegundos(h, m, s):
    segundos = (h*60*60) + (m*60) + s
    return segundos

h = float(input("Horas: "))
m = float(input("Minutos: "))
s = float(input("Segundos: "))

print("O total de segundos é de {0} segundos".format(totalSegundos(h, m, s)))