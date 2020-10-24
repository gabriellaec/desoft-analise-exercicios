dias = int(input("Digite dias: "))
hor = int(input("Digite horas: "))
mint = int(input("Digite minutos: "))
seg = int(input("Digite segundos: "))


total_mint = mint*60
total_hor = hor*3600
total_dias = dias*86400

total = seg + total_mint + total_hor + total_dias

print(total)
