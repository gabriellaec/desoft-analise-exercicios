fuma_por_dia = int(input('Quantos cigarros você fuma por dia? '))
quantos_anos_fuma = int(input('A quantos anos você já fumaa? '))

quanto_ja_fumou = fuma_por_dia * 365 * quantos_anos_fuma

tempo_perdido_minutos = (quanto_ja_fumou * 10)
tempo_perdido = tempo_perdido_minutos / 60*24
print(tempo_perdido)