v=int(input('Velocidade: '))
a=int(input('Angulo: '))
import math
def dist(v,a):
    d=(v**2)*(math.sin(a*math.pi/180))/10
    if d<100:
        return 'Muito perto'
    if d==100:
        return 'Acertou!'
    else:
        return 'Muito longe'
print(dist(v,a))
    
        
    
    