from math import *
tempo_minimo=1000000
nome=input("Digite o nome de um atleta: ")
while not nome=="sair":
    aceleracao=int(input("Digite a aceleracao: ")) 
    nome=input("Digite o nome de um atleta: ")
    tempo=sqrt((2*100)/aceleracao)
    if tempo<tempo_minimo:
        vencedor=nome
        tempo_minimo=tempo

print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor, tempo_minimo)) 