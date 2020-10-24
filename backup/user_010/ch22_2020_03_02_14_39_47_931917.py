cig_dia = int (input("Quantos cigarros você fuma por dia?"))
anos = int (input("Há quantos anos você fuma?"))
cig = cig_dia * (365 * anos)
vida_min = cig * 10
vida_dia = vida_min/1440
print ("Você ja perdeu {0} em minutos de vida, ou seja, aproximadamente {1:.0f} dias.".format (vida_min,vida_dia))