a = (int(input("Dias")))
b = (int(input("Horas")))
c = (int(input("Minutos")))
d = (int(input("Segundos")))
     
asegundos = a * 86400
bsegundos = b * 3600
csegundos = c * 60

z = asegundos + bsegundos + csegundos + d
print (z)