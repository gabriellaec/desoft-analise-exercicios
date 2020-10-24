cigarros_por_dia = int(input("Cigarros fumados por dia "))
anos_fumando = int(input("Anos fumando cigarros "))

dias = anos_fumando*365
cigarros = dias*cigarros_por_dia
minutos_perdidos = cigarros*10
dias_perdidos = minutos_perdidos/(60*24)
print(dias_perdidos)
