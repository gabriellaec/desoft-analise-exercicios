cigarros = int(input("Quantos cigarros você fuma por dia?"))
anos = int(input("Há quantos anos você fuma?"))
vida_perdida = cigarros * anos * 365 * 10 / 1440
print("você já perdeu {0} dias de vida" .format(vida_perdida))