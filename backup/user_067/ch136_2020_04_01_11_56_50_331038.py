import random

dinheiro = 10
aux = dinheiro
if(aux>0):
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = random.randint(1,6)
    soma = x + y + z
    print(soma)
    print('Você possui 10 dinheiros')
    resp = str(input('Você quer ima dica?'))
    while(resp == 'sim')and(aux>0):
        aux-=1
        a = int(input('Escolha um número'))
        b = int(input('Escolha um número'))
        c = int(input('Escolha um número'))
        
        if((soma==a)or(soma==b)or(soma==c)):
            print('Está entre os 3')
            dinehiro=aux
        else:
            print('Não está ente os 3')
            diheiro=aux
        resp = str(input('Você quer ima dica?'))
    if(resp=='não'):
        print('Você tem {} dinheiros.'.format(aux))
        while(aux>0):
            chute = int(input('Chute um número: '))
            aux-=1
            if(chute==soma):
                print('Você ganhou o jogo com {} dinheiros'.format(5*aux))
                break
        dinheiro=0
        if (aux==0 and dinheiro==0):
            print('Você perdeu!')      
else:
    print('Você perdeu')