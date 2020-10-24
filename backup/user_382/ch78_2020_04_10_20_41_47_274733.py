import math as m 
def calcula_tempo(dic):
    dic2 = {}
    for i in dic:
        dic2[i] = m.sqrt(200/dic[i])
    return dic2

dic = {}
dic2 = {}

while True:
    resp = input('Qual o nome do atleta?: ')
    if resp == 'sair':
        break
    else:
        dic[resp] = input('Qual a acelereção do atleta?: ')

dic2 = calcula_tempo(dic)
tmin = min(dic.values())
atleta = dic.keys(tmin)    

print(' vencedor é {0} com tempo de conclusão de {1} s'.format(atleta, tmin))