import random
d=10
jogo=True
while (jogo):
    if d>0:
        print('Seu dinheiro: {0]'.format(d)
        if d==0:
            jogo=False
        else:
            while d<=10:
              a=random.randint(1, 6)
              b=random.randint(1, 6)
              c=random.randint(1, 6)
              somadados=a+b+c
              resposta=input('Advinha o numero das somas dos numeros: ')
            if resposta==somadados:
              input('Você ganhou o jogo com {0}'.format(d)
            else:
                y=input('Você quer uma dica? ')
                  if y=='sim':
                    g=input('Fale um numero ')
                    h=input('Fale um numero ')
                    j=input('Fale um numero ')
                    if g or h or j==somadados:
                        print('Está entre os 3')
                    elif:
                        print('Não está entre os 3')
            if y=='não':
               
                        
                    
                  
                    
              
              