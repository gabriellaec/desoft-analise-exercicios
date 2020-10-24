cigarros= int(input( "quantos cigarros voce fuma por dia: "))
anos= int(input( "a quantos anos voce fuma: "))
cigarros= (cigarros*(anos*365))
tempo_min= (cigarros*10)
tempo_perdido= (tempo_min/(60*24))

print("voce perdeu {0} dias de vida".format(tempo_perdido))