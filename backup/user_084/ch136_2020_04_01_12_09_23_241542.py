from random import randint
d1=randint(1,2,3,4,5,6)
d2=randint(1,2,3,4,5,6)
d3=randint(1,2,3,4,5,6)
x==d1+d2+d3
i=10
print(i)
dica=input('Você quer uma dica? Ela custa uma vida. ')
if dica=='sim':
    while i>10:
        chuted1=input('escolha uma possivel soma')
        chuted2=input('escolha uma possivel soma')
        chuted3=input('escolha uma possivel soma')
        if x==chute1 or x==chute2 or x==chute3:
            print('está entre os 3')
        else:
            print('não está entre os três')
        i-=1
elif dica=='não':
    print(i)
    if i>0:
        chute=('chute um numero')
        if chute==x:
            print('voce ganhou o jogo')
    else:
        print('voce perdeu o jogo')
        
        
        
            
            
    
