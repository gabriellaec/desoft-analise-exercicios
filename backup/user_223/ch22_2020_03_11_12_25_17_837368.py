cig = int(input("Quantos cigarros você fuma por dia? "))
tempo = int(input("Há quantos anos você fuma? "))

rouba_dias = (cig*0.00694444*tempo*365)

print("Você perdeu {0:.0f} dias de vida ".format(rouba_dias))