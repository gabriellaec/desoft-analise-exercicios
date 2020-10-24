v=int(input("Qual foi a velocidade da jaca?"))
a=int(input("Qual foi o angulo de lancamento da jaca?"))
import math 
d=v**2*math.sin(2*a)/9.8 
if d>=82 and d<=102:
    print('Acertou!')
elif d<82:
    print ('Muito perto')
else:
    print ('Muito longe')
    
