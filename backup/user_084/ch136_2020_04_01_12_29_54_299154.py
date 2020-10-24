from random import randint
d1=randint(1,2,3,4,5,6)
d2=randint(1,2,3,4,5,6)
d3=randint(1,2,3,4,5,6)
x==d1+d2+d3
i=10
while i>10:
    print(i)
    dica=input('Você quer uma dica? Ela custa uma vida. ')
    if dica=='sim':
        chuted1=input('escolha uma possivel soma')
        chuted2=input('escolha uma possivel soma')
        chuted3=input('escolha uma possivel soma')
        if x==chute1 or x==chute2 or x==chute3:
            print('está entre os 3')
            escolha=input('escolha um dos tres')
            if escolha==x:
                print('voce ganhou o jogo')
                i=i*6
                 print('voce ganhou o jogo com x dinheiros')
        else:
            print('não está entre os três')
        i-=1
    elif dica=='não':
        print(i)
        while i>0:
            chute=input('chute um numero')
            if chute==x:
                print('você ganhou o jogo')
                i=i*6
            else:
                i-=1
            print('voce ganhou o jogo com x dinheiros')
print('voce perdeu o jogo')

            
        
         
        
        
        
            
            
    
