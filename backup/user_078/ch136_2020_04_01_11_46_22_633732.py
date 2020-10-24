import random
dinheiro = 10
jogo = True

while jogo
    dadoUm = random.randint(1,6)
    dadoDois = random.randint(1,6)
    dadoTres = random.randint(1,6)
    somaDados= dadoUm+dadoDois+dadoTres
    
    if dinheiro>0:
        print ('Seu dinheiro:{0}'.format(dinheiro))
        a = str(input('Você quer uma dica? Cada dica custa 1 dinheiro(sim/não) '))
        
        #começa fase de dicas
        if a == 'sim':
            dinheiro = dinheiro - 1
            numeroUm = int(input('Insira um número: '))
            numeroDois = int(input('Insira um número: '))
            numeroTres = int(input('Insira um número: '))
            
            if somaDados==numeroUm or somaDados==numeroDois or somaDados==numeroTres:
                print('Está entre os 3')   
            else:
                print('Não está entre os 3')
        
        #começa fase de chutes
        else a=='não':
            print ('Seu dinheiro:{0}'.format(dinheiro))            
            if dinheiro<=0:
                jogo = False 
                
            #chuta um número
            else:
                chute = int(input('Chute um número: '))
                if chute == somaDados:
                    dinheiro=dinheiro+dinheiro*5
                    #termina o jogo
                else: 
                    if chute != somaDados
                    dinheiro = dinheiro-1
                    #retorna para a fase de chutes
        
        
        
    else:
        jogo = False