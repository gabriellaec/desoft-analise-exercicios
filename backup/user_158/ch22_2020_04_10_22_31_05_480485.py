Cigarros_por_dia  = int(input("quantos cigarros por dia voce fumma"))
Tempo_fumando = int(input("ha quantos anos voce fuma ?")) 
tempo_perdido = (10*Cigarros_por_dia*Tempo_fumando*365)/1440
print("voce perdeu {0} anos de sua vida".format(tempo_perdido))
