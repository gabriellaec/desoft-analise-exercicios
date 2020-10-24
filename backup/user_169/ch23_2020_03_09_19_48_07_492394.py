velocidade=int(input("Qual é a velocidade do carro?"))

if velocidade>80:
    return "você foi multado" and (velocidade - 80)*5

else:
    return "Não foi multado"