import math
def calcula_tempo(atletas):
    dic = {}
    for k,v in atletas.items():
        t = math.sqrt(200/v)
        dic[k] = t
    return dic
d = {}
o = True
while o:
    atleta = input('nome do atleta: ')
    if atleta == 'sair':
        o = False
    else:
        ac = int(input('aceleração: '))
        d[atleta] = ac 
time = calcula_tempo(d)
max = 0
vencedor = 'ninguem'
for k,v in time.items():
    if v > max:
        max = v
        vencedor = k
print(f'O vencedor é {vencedor} com tempo de conclusão de {max} s')

