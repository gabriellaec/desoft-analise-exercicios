cig = int(input("Quantos cigarros você fuma por dia? "))
tempo = int(input("Há quantos anos você fuma? "))

rouba_dias = (cig*10*tempo*365*24)

print("Você perdeu {} minutos de vida ".format(rouba_dias))