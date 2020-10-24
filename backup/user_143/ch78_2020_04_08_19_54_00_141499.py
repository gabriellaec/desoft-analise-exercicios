n='n'
d={}
while n!='sair':
    n=input('Qual o nome:')
    if n!='sair':
        a=float(input('Qual a aceleração:'))
        d[n]=a
def  calcula_tempo (d):
    dici={}
    for v,i in d.items():
        r=v
        t=(200/i)**(1/2)
        dici[r]=t
    return dici
dici=calcula_tempo(d)
k=0
for b,g in dici.items():
    if g>k:
        x=b
        k=g
print('O vencedor é {0} com tempo de conclusão {1}'. format(x, k))
        
    
