cigarros_dia = int(input("Quantos cigarros fumados por dia"))

anos_fumados = float(input("Quantos anos você fumou"))

cigarro_minuto = cigarros_dias / (24 * 60)

minutos_fumados = anos_fumados / (365 * 24 * 60)

tempo_perdido = cigarro_minuto * minutos_fumados * 10

print(tempo_perdido)