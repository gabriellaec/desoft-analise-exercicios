cigarros = int(inpu("Quantos cigarros você fuma por dia?: "))
anos = int(input("Há quantos você fuma?: "))
cigarros = (cigarros*(anos*365))
minutos = cigarros * 10 
tempo_perdido = minutos/(60*24)

print("Você perdeu {0} dias de vida.".format(tempo_perdido))