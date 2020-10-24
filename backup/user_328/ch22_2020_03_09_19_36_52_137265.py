cigarros= int(input("quantos cigarros você fuma por dia: "))
anos= int(input("a quantos anos você fuma: "))
cigarros= (cigarros*(anos*365))
minutos= (cigarros*10)
tempo_perdido= (minutos/(60*24))

print("você perdeu {0} dias de vida".format(tempo_perdido))