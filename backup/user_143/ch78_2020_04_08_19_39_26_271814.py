n='n'
d={}
while n!='sair':
    n=input('Qual o nome:')
    if n!='sair':
        a=float(input('Qual a aceleração:'))
        d[n]=a
print(d)
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
        k=g
        
    
