d = int(input("Dias: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))

def calsegundos(Dias, Horas, minutos):
    segundos = (Dias*86400)+(Horas*3600)+(minutos*60)
    return (segundos)

print(calsegundos(d, h, m))