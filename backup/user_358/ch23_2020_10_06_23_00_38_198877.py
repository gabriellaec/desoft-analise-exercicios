velocidade=int(input('qual a velocidade do carro do usuario? '))
if velocidade>80:
    a=velocidade-80
    b=a*5
    print(f'R${b:.2f} ')
else:
    print('Não foi multado')