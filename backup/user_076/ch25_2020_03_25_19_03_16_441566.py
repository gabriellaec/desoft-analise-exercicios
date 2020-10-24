import math

velocidade = int(input ("Com qual velocidade, em m/s, você deseja lançar a jaca?"))
ângulo = int(input ("Com qual ângulo, em graus, você deseja lançar a jaca?"))

def distância(v,teta):
    senorad = math.sin(2*teta)
    senograus = ( senorad * 360 ) / (2 * math.pi)
    d = ( v**2 * senograus ) / 9.8
    return d

if 98 <= distância(velocidade, ângulo) <= 102:
    print ('Acertou!')
elif distância(velocidade, ângulo) < 98:
    print ("Muito perto")
elif distância(velocidade,ângulo) > 102:
    print ("Muito longe")
      