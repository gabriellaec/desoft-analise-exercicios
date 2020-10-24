cigarros_dia = int(input("cigarros por dia: "))
tempo_de_fumante = int(input("quantos anos fuma: "))
dias_perdidos = (cigarros_dia*10*tempo_de_fumante*365)/(24*60)
print("você perdeu {0} dias de vida".format(dias_perdidos))
