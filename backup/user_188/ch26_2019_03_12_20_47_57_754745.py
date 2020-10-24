def tempo(dias, horas, minutos, segundos):
    horas = horas + 24*dias
    minutos = minutos + 60*horas
    segundos = segundos + 60*minutos
    return segundos

d = int(input("Dias: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
print(tempo(d, h, m, s))