num_cig = int(input("Quantos cigarros você fuma por dia? "))
ano_fum = int(input("Há quantos anos você fuma? "))
qntd_cigarros = (ano_fum*365)*num_cig
tempo_perdido = (qntd_cigarros*10)/1440
print("Você perdeu {0:.0f} dias de vida por causa do cigarro.".format(tempo_perdido))