import math
v=int(input("Insira a velocidade da jaca "))
tetha=int(input("Insira o ângulo de lançamento "))
g=int(9.8)
d=((v**2)*math.sin(2*tetha))/g

if d<float(98):
    print('Muito perto')
elif float(98)<=d<=float(102):
    print('Acertou!')
elif d>float(102):
    print('Muito longe')

            


            
