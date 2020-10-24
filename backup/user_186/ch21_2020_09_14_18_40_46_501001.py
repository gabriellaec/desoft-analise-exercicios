d = int(input("Dia ")
h = int(input("Hora ")
m = int(input("Minuto ")
s = int(input("Segundo ")
def calcula_segundos (d, h, m, s) :
    y = (d*24)/3600 + h/3600 + m/60 + s
    return y
print y