velocidade=int(input('qual a velocidade do carro do usuario? '))
if velocidade>80:
    a=velocidade-80
    b=a*5
    print(b)
else:
    print('Não foi multado')