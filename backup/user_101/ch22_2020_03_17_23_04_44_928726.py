num_cigarros=int(input("Quantos cigarros você fuma por dia? "))
anos_fumando=int(input("Fuma a quantos anos? "))
tempo_em_dez_minutos=anos_fumando*365*24*6
total_cigarros=num_cigarros*anos_fumando*365
dias_perdidos=(total_cigarros*tempo_em_dez_minutos)/(60*24)
print(dias_perdidos)