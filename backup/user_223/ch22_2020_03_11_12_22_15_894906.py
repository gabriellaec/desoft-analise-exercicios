cig = int(input("Quantos cigarros você fuma por dia? "))
tempo = int(input("Há quanto tempo você fuma? "))

rouba_min = (cig*10*tempo*365*24*60)

print("Você perdeu {0} minutos de vida ".format(rouba_min))