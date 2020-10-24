d = int(input("Quantos cigarros você fuma por dia? "))
a = int(input("Você fuma há quantos anos? "))
total_cigarros = a*d
minutos_perdidos = total_cigarros*10
total_perdido = minutos_perdidos/1440
print("Você já perdeu {0} anos de sua vida".format(total_perdido))
