import math
lnome=[]
lacel=[]
r1=input('Nome:')
lnome.append(r1)
r2=int(input('Velocidade:'))
lacel.append(r2)
while not r1=='sair':
    r1=input('Nome:')
    lnome.append(r1)
    if r1=='sair':
        None
    else:
        r2=int(input('Velocidade:'))
        lacel.append(r2)
ltem=[]
for i in lacel:
    v=math.sqrt(200/i)
    ltem.append(v)
        
t=1
x=ltem[0]
while t<len(ltem):
    if x<ind[t]:
        x=ind[t]
    else:
        None
    t+=1    
vencedor=lnome[ltem.index(x)]
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(vencedor,x))