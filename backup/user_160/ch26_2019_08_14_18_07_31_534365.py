dias = input("Quantos dias?")
horas = input ("Quantas horas?")
minutos = input("Quantos minutos")
segundos = input("Quantos segundos?")
               
def segundostotal(dias, horas, minutos, segundos):
               y = segundos + minutos*60 + horas*360 + dias*8640
               print( y)