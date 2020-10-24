dias = int(input("Quantos dias?"))
horas = int(input ("Quantas horas?"))
minutos = int(input("Quantos minutos"))
segundos = int(input("Quantos segundos?"))
               
def segundostotal(dias, horas, minutos, segundos):
               y = segundos + minutos*60 + horas*360 + dias*8640
               return y