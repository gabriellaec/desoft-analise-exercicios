m = int(input('Qual a velocidade?'))
n = int(input('Qual o ângulo?'))
import math
def distancia(v,θ):
    y = ((v**2)*(math.sin(math.radians(2*θ))))/(9.8)
    if y < 98:
        return 'Muito perto!'
    elif y >= 98 and y <= 102:
        return 'Acertou!'
    else:
        return 'Muito longe!'
print(distancia(m,n))
     
    
