fuma_por_dia = int(input('Quantos cigarros você fuma por dia? '))
quantos_anos_fuma = int(input('A quantos anos você já fuma? '))

quanto_ja_fumou = fuma_por_dia * 365 * quantos_anos_fuma

tempo_perdido = quanto_ja_fumou / 144
print(tempo_perdido)