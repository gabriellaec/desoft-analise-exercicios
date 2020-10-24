percorrer_km = float(input("Quantos quilômetros você quer percorrer? "))
if percorrer_km < 200:
    print("Preco da passagem: {0}".format(round((percorrer_km*0.5), 2)))
else:
    print("Preco da passagem: {0}".format(round(((percorrer_km * 0.5) + 0.45*(200 - percorrer_km)), 2)))