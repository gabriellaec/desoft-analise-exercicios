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
    
    
