d = int(input("Distância em km: "))
valor = 0
if d <= 200:
    valor = d * 0.5
elif d > 200:
    valor = 100 + 0.45 * (d - 200)
print(valor)