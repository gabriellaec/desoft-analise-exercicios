velocidade=float(input("Qual a velocidade?"))
if velocidade>80:
    
    print("multa de {0:.2f}".format((velocidade-80)*5))
else:
    print("Não foi multado")
    
