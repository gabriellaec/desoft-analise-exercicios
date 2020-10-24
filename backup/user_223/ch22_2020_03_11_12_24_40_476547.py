cig = float(input("Quantos cigarros você fuma por dia? "))
tempo = float(input("Há quantos anos você fuma? "))

rouba_dias = (cig*0.00694444*tempo*365*24)

print("Você perdeu {0:.0f} minutos de vida ".format(rouba_dias))