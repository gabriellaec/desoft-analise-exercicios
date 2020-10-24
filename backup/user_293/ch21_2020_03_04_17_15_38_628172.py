seg = int(input("Digite segundos: "))
mint = int(input("Digite minutos: "))
hor = int(input("Digite horas: "))
dias = int(input("Digite dias: "))

total_mint = mint*60
total_hor = hor*3600
total_dias = dias*86400

total = seg + total_mint + total_hor + total_dias

print(total)
