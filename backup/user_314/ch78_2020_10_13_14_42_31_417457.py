import math

def calcula_tempo(dic):

    dic_tempo={}

    for i in dic.keys():
        dic_tempo[i]=math.sqrt(2*100/dic[i])

    return dic_tempo

atleta=dict(input("Digite o nome e a aceleração dos atletas (sair=fim): "))

tempo= calcula_tempo(atleta)

vencedor= min(tempo.values())

print('O vencedor é {0} com tempo de conclusão de {} s'.format(atleta[vencedor]),vencedor)