def calcula_tempo(atletas):
    v={}
    for e in atletas:
        x=atletas[e]
        v[e]=(200/x)**0.5
    return v
atletas={'a': 8, 'b':10,'c':15}
print(calcula_tempo(atletas))

dicionario={}
nome='oi'
while nome != 'sair':
        nome=input('nome')
        if nome != 'sair':
            aceleracao=int(input('aceleracao'))
            dicionario[nome]=aceleracao
    
t=calcula_tempo(dicionario)
minimo=min(t.values())
for a,temp in t.items():
    if temp==minimo:
        print('O vencedor é {0} com tempo de conclusão de {1} s'.format(a,temp))