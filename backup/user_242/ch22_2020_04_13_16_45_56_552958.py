cigarros = int(input("Quantos cigarros você fuma por dia?: "))
anos = int(input("Há quantos você fuma?: "))
cigarros_total = (cigarros*(anos*365))
minutos_perdidos = cigarros_total * 10 
tempo_perdido = minutos_perdidos/(60*24)

print("Você perdeu {0} dias de vida.".format(tempo_perdido))