import math

velocidade = float(input("Qual a velocidade da jaca? "))
ângulo = float(input("Qual o ângulo de lançamento da jaca? "))
distância = ((velocidade**2)*(math.sin(2*ângulo)))/(9.8)
if distância < 99 :
    print('Muito perto')
elif 99 <= distância <= 101 :
    print('Acertou!')
else : 
    print('Muito longe')