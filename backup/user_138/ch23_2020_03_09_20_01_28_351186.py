velocidade=float(input("Qual a velocidade?"))
velo=(velocidade-80)*5
if velocidade>80:
    print("multa de%.2f",%velo)
else:
    print("Não foi multado")