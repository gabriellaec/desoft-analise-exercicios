import math

def calcula_tempo(dic):

    dic_tempo={}

    for i in dic.keys():
        dic_tempo[i]=math.sqrt(2*100/dic[i])

    return dic_tempo

def menor_tempo(dic):
    m=list(dic.values())
    minimo=m[0]

    for i in dic.values():
        if(i<minimo):
            minimo=i
    
    return minimo

atleta={}
i=''

while(i != 'sair'):
    i=input("Nome: ")
    
    if(i != 'sair'):
        t=int(input("aceleração: "))
        atleta[i]=t

tempo= calcula_tempo(atleta)
vencedor=menor_tempo(tempo)

for i in tempo.keys():
    if(tempo[i]==vencedor):
        print('O vencedor é {0} com tempo de conclusão de {1} s'.format(i,tempo[i]))