dia=int(input("Quantos dias?"))
horas=int(input("Quantas horas?"))
minutos=int(input("Quantos minutos?"))
segundo=int(input("E quantos segundos?"))

tempo=segundo+minutos*60+horas*60*60+dia*24*60*60
print("O tempo que você descreveu corresponde a {0} segundos".format(tempo))