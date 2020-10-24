cigarros=int(input("Quantos cigarros fuma por dia?"))
tempo=int(input("Há quantos anos fuma?"))
perdido=(cigarros*10)*tempo*365*cigarros
print("Você já perdeu {0} minutos, fumando {2} cigarros durante {1} anos".format(perdido, tempo, cigarros))