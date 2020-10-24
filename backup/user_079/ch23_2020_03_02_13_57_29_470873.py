
velocidade=int(input('velo?:'))
if velocidade>80:
    multa=(velocidade-80)*5
    print("%.2f" % multa)
else:
    print('Não foi multado')