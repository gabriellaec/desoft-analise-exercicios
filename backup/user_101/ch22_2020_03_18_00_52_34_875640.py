num_cigarros=int(input("Quantos cigarros você fuma por dia? "))
anos_fumando=int(input("Fuma a quantos anos? "))
total_cigarros=num_cigarros*(anos_fumando*365)
minutos_perdidos=total_cigarros*10
dias_perdidos=minutos_perdidos/(60*24)
print(dias_perdidos)