a=float(input("velocidade:"))
if a > 80:
    y=5*(a-80)
    print("voce foi multado em:",{0:.2f} format (y))
else:
    print("Não foi multado")