import math

velocidade = float(input ("Com qual velocidade, em m/s, você deseja lançar a jaca?"))
ângulo = float(input ("Com qual ângulo, em graus, você deseja lançar a jaca?"))

def distância(v,teta):
    d = ( v**2 * math.sin(2*teta) ) / 9.8
    return d

if distância(velocidade, ângulo) == 100:
    print ('Acertou!')
elif 100 > distância(velocidade, ângulo) > 98:
    print ("Muito perto")
else:
    print ("Muito longe")
      