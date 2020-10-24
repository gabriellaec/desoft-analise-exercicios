num_cigarros=int(input("Quantos cigarros você fuma por dia? "))
anos_fumando=int(input("Fuma a quantos anos? "))
tempo_em_dez_minutos=anos_fumando*365*24*6
dias_perdidos=(num_cigarros*tempo_em_dez_minutos)/(60*24)
print(dias_perdidos)