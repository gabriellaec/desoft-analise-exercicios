mport math    
g=9.8
v=float(input('velocidade?: '))
angulo=float(input('angulo?: '))
rad=(math.pi/180)*angulo
d=((v**2)*math.sin(2*rad))/g
if (d<=102 and d>=98):
    print("Acertou")
elif (d<98):
    print ('Muito perto')
else:
    print('Muito longe')