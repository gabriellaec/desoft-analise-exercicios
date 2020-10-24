import math
diciok=[]
diciov=[]
continua=True
while continua:
    r=input('Digite um nome')
    diciok.append(r)
    if r=='sair':
        break
    u=input('Digite uma aceleracao')
    diciov.append(int(u))
dicio=dict(zip(diciok,diciov))

def calcula_tempo(dicio):
    k=dicio.keys()
    v=list(dicio.values())
    d=[0]*len(v)
    for i in range(len(v)):
        d[i]=math.sqrt(200/v[i])
    n=dict(zip(k, d))
    j=min(n.values())
    for chave,valor in n.items():
        if valor==j:
            return print('O vencedor é {0} com tempo de conclusão de {1} s'.format(chave,j))