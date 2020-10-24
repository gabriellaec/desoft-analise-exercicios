cig = int(input("Quantos cigarros você fuma por dia? "))
tempo = int(input("Há quanto tempo você fuma? "))

rouba_min = (cig*10*tempo*365*24*60)
rouba_dias = (cig*0.00694444*tempo*365)
print("Você perdeu {0} minutos de vida ({1:.0f} dias) ".format(rouba_min, rouba_dias))