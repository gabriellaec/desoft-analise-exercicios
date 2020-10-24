import math
x = float(input('Qual a velocidade e o ângulo de lançamento da jacosa?')
def distancia_da_jaca(v, θ):
          d = (v**2 * math.sin(2*θ)) / 9.8
          if d < 98:
              return 'Muito perto'
          elif d > 102:
              return 'Muito longe'
          else:
              return 'Acertou!'