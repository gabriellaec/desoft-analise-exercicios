distance = float(input("Qual a distância, em quilometros, da sua viagem?"))
price = distance

if distance <= 200:
    price *= 0.50
else:
    price = (price - 200) * 0.45 + 200 * 0.50

print("{0.2f}".format(price))
