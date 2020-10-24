# redução do tempo de vida em dias a partir do número de cigarros?
# quantos anos fuma? quantos cigarros por dia?
# 1 cigarro = -1/(24*6) dia de vida
# 1dia = 24*60 min

c = int(input('quantos cigarros por dia'))
a = (int(input('quantos anos fuma')))*365
tempo_de_vida = a*c*(1/(24*6))
print(tempo_de_vida)
