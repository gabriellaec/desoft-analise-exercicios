import math
def calcula_tempo(dic):
    resultado_prova = {}
    for i in dic:
        tempo = math.sqrt((100*2)/dic[i])
        resultado_prova[i]=tempo
    return resultado_prova
corrida = {}
nome = input('nome do corredor')
aceleracao = input('aceleracao do corredor')
while nome != 'sair':
    corrida[nome]= aceleracao
    nome = input('nome do corredor')
    if nome != 'sair':
        aceleracao = input('aceleracao do corredor')
menor_tempo=100000
vencedor =''
for corredor,tempo in corrida.items():
    if tempo < menor_tempo:
        menor_tempo = tempo
        vencedor = corredor 
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,menor_tempo))
