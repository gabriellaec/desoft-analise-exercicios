import math

velocidade = int(input ("Com qual velocidade, em m/s, você deseja lançar a jaca?"))
ângulo = int(input ("Com qual ângulo, em graus, você deseja lançar a jaca?"))

def distância(v,teta):
    ângulorad =  (teta * math.pi) / 180
    senorad = math.sin(2*ângulorad)
    senograus = ( senorad * 180 ) / (math.pi)
    d = ( v**2 * senograus ) / 9.8
    return d

if 98 <= distância(velocidade, ângulo) <= 102:
    print ('Acertou!')
elif distância(velocidade, ângulo) < 98:
    print ("Muito perto")
elif distância(velocidade,ângulo) > 102:
    print ("Muito longe")
      