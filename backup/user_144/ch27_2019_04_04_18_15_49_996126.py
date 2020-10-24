cig = int(input("Quantos cigarros vc fuma por dia? "))
ano = int(input("Quantos anos voce fuma? " ))

total_cig = (ano * 365) * cig
dias_perdidos = (total_cig * 10 / 24)

print("Dias perdidos {0} , ".format(cig,ano))
