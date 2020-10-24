cigarros=int(input("Quantos cigarros fuma por dia?"))
tempo=int(input("Há quantos anos fuma?"))
perdido=cigarros*10*tempo*365*
print("Você já perdeu {0} dias, fumando {2} cigarros durante {1} anos".format(perdido, tempo, cigarros))