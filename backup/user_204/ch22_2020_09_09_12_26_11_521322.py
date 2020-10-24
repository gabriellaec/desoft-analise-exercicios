'''
22. Redução no tempo de vida de um fumante
Escreva um programa que calcule a redução de tempo de vida de um fumante a partir do número de cigarros. 
Pergunte quantos cigarros ele fuma por dia e há quantos anos fuma. Imprima o tempo de vida perdido em dias. 
Considere que um cigarro rouba 10 minutos de expectativa de vida.
'''
cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Ha quantos anos você fuma? "))
anos_cigarros = int((anos_fumando * 365) * cigarros)
total = int((anos_cigarros * 10))
total_dias = (total / 1440)
print(f"{total_dias:.2f}")