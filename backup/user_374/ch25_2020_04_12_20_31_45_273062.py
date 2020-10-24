import math

v = float(input('Digite um valor de aceleração '))
teta = float(input('Digite um valor para o ângulo '))


calculo =((v**2)*math.sin(2*math.radians(teta)))/9.8
    
if calculo == 100:
        print('Acertou!')
elif calculo > 102:
        print('Muito longe')
elif calculo < 98:
        print('Muito perto')
