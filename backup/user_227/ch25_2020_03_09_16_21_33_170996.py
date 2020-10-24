import math

velocidade = float(input("Qual a velocidade da jaca? "))
ângulo = float(input("Qual o ângulo de lançamento da jaca? "))
distância = ((velocidade**2)*(math.sin(2*math.degrees(ângulo)))/(9.8)
if distância < 98 :
    print('Muito perto')
elif 98 <= distância <= 100 :
    print('Acertou!')
else : 
    print('Muito longe')