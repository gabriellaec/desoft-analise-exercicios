velocidade=float(input("Qual a velocidade do carro"))
if velocidade>80:
    multa=5*(velocidade-80)
    print (f'multa:{multa:.2f}')
else:
    "Não foi multado"
 