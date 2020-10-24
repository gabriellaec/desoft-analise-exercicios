km = float(input("Quantos KM?"))

if km>80:
    Round(Valor = (km-80)*5, 2)
    print("MULTADO, R${0}" .format(Valor))
else:
    print("Não foi multado")