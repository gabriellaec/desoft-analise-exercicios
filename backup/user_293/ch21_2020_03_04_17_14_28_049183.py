seg = int(input("Digite segundos: "))
mint = int(input("Digite minutos: "))
hor = int(input("Digite horas: "))
dias = int(input("Digite dias: "))

total_mint = seg/60
total_hor = total_mint/60
total_dias = toral_hor/24

total = seg + total_mint + total_hor + total_dias

print(total)
