d = int(input("Dias: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))
j = int(input("Segundos: "))

def calsegundos(Dias, Horas, minutos, segundos):
    segundo = (Dias*86400)+(Horas*3600)+(minutos*60)+ segundos
    return (segundo)

print(calsegundos(d, h, m , j))