velocidade=float(input("Qual a velocidade?"))
if velocidade>80:
    print("multa de",((velocidade-80)*5))%.2f
else:
    print("Não foi multado")