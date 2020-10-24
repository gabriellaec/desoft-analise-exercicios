km = float(input("Quantos KM?"))

if km>80:
    Valor = (km-80)*5
    print("MULTADO, R${0:.02f}" .format(Valor))
else:
    print("Não foi multado")