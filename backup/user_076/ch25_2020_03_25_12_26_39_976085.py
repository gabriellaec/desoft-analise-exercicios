import math

velocidade = float(input ("Com qual velocidade, em m/s, você deseja lançar a jaca?"))
ângulo = float(input ("Com qual ângulo, em graus, você deseja lançar a jaca?"))

def distância(v,teta):
    d = ( v**2 * math.sin(2*teta) ) / 9.8
    return d

if 98 <= distância(velocidade, ângulo) <= 102:
    print ('Acertou!')
elif distância(velocidade, ângulo) < 98:
    print ("Muito perto")
else:
    print ("Muito longe")
      