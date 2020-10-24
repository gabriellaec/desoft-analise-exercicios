cigarros_por_dia = int( input("Cigarros por dia: ") )
anos_fumando = int( input("Anos fumando: ") )

# 365 = dias em um ano
cigarros_no_total = cigarros_por_dia * anos_fumando * 365

# reducao de vida em minutos
reducao_de_vida = cigarros_no_total * 10

# conversao de minutos para dias
# 1440 = minutos em um dia
reducao_de_vida /= 1440

print(reducao_de_vida)
