import math

velocidade = input ("Com qual velocidade, em m/s, você deseja lançar a jaca?")
ângulo = input ("Com qual ângulo, em graus, você deseja lançar a jaca?")

def distância(v,teta):
    d = ( v**2 * sin(2*teta) ) / 9.8
    return d

if d == 100:
    print 'Acertou!'
elif d==98:
    print "Muito perto"
else:
    print "Muito longe"