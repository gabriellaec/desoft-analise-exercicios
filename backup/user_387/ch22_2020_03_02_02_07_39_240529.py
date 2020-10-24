cigarros_por_dia = float(input("Quantos cigarros fuma por dia: "))

tempo_fumando = float(input("há quantos anos fuma: "))

tempo_fumando_em_dias = tempo_fumando * 365

cigarros_fumados = tempo_fumando_em_dias * cigarros_por_dia

tempo_perdido_em_dias = (cigarros_fumados * 10) / 1440



print("O Tempo perdido fumando foi de", tempo_perdido_em_dias, "dias")