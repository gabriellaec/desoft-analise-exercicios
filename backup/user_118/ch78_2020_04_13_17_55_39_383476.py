import math
def calcula_tempo(atletas):
    dic={}
    for k, v in atletas.items():
        t=math.sqrt(200/v)
        dic[k]=t
    return dic
d={}
o=True
while o:
    atleta = input('Nome do atleta: ')
    if atleta == 'sair':
        o=False
    else:
        ac = int(input('Aceleração: '))
        d[atleta]=ac
time = calcula_tempo(d)
max=10000
vencedor='ninguem'
for k, v in time.items():
    if v<max:
        max=v
        vencedor=k
print ('O vencedor é {vencedor} com tempo de conclusão de {max} s')
                 
