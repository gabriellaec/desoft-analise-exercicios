cig = float(input("Quantos cigarros você fuma por dia? "))
tempo = float(input("Há quantos anos você fuma? "))

rouba_dias = (cig*(10/1440)*tempo*365)

print("Você perdeu {} dias de vida ".format(rouba_dias))