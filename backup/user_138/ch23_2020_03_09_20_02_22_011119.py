velocidade=float(input("Qual a velocidade?"))
if velocidade>80:
    velo=(velocidade-80)*5
    print("multa de%.2f",%velo)
else:
    print("Não foi multado")