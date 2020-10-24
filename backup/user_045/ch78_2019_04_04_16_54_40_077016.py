k=input('qual nome?')
n={}
while k!='sair': 
    v=float(input('qual valor?'))
    n[k]=v
    k=input('qual nome?')
d={}

s=5000000000
for nome,aceleracao in n.items():
    d[nome]=(200/aceleracao)**0.5
    for nome,tempo in d.items():
        if s>tempo:
            s=tempo
            t=nome
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(t,s))
    
