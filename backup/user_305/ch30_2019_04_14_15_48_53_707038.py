v = int(input('Velocidade da jaca'))
a = int(input('Angulo de lançamento'))
import.math
d = (v**2*math.sin(2*a))/9.8
if d >= 102:
    print ('Muito longe')
elif d<=98:
    print ('Muito perto')
else:
    print ('Acertou!')
