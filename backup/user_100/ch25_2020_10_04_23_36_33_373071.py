import math
v = float(input('Qual a velocidade e de lançamento da jacosa? '))
θ = float(input('Qual o ângulo de lançamento da jacosa? '))
def distancia_da_jaca(v, θ):
   
    
    d = (v**2 * math.sin(math.radians(2 * θ))) / 9.8
    if d < 98:
        print('Muito perto') 
    elif d > 102:
        print('Muito longe') 
    else:
        print('Acertou!')





