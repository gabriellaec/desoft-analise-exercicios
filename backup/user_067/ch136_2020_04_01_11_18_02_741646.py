import random
random.seed()

dinheiro = 10
aux = dinheiro
if(aux>0):
    x = random.randint()
    y = random.randint()
    z = random.randint()
    soma = x + y + z
    print('Você possui 10 dinheiros')
    resp = str(input('Você quer ima dica?'))
    if(resp == 'sim'):
        aux-=1
        a = str(input('Escolha um número'))
        b = str(input('Escolha um número'))
        c = str(input('Escolha um número'))
        if((soma==a)or(soma==b)or(soma==c)):
            print('Está entre os 3')
            dinehiro=aux
        else:
            print('Não está ente os 3')
            diheiro=aux
            aux=0
    elif(resp=='não'):
        print('Você tem {} dinheiros.'.format(dinheiro))
        while(dinheiro>0):
            chute = str(input('Chute um número: '))
            if(chute==soma):
                print('Você ganhou o jogo com {} dinheiros'.format(5*dinheiro))
                dinheiro=0
        if(dinheiro==0):
            print('Você perdeu')           
else:
    print('Você perdeu')