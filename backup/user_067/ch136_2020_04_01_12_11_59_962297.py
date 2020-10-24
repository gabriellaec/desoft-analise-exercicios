import random

dinheiro = 10
aux = dinheiro
if(aux>0):
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = random.randint(1,6)
    soma = x + y + z
    print('10')
    resp = str(input('Você quer uma dica?'))
    while(resp == 'sim')and(aux>0):
        aux-=1
        print(aux)
        a = int(input('Escolha um número'))
        b = int(input('Escolha um número'))
        c = int(input('Escolha um número'))
        
        if((soma==a)or(soma==b)or(soma==c)):
            print('Está entre os 3')
            dinehiro=aux
        else:
            print('Não está entre os 3')
            diheiro=aux
        resp = str(input('Você quer uma dica?'))
    if(aux==0):
        print('perdeu')
        
    if(resp=='não'):
        while(aux>0):
            print(aux)
            chute = int(input('Chute um número: '))
            if(chute==soma):
                print('Você ganhou o jogo com {} dinheiros'.format(aux + 5*aux))
                break
            aux-=1
        dinheiro=0
        if (aux==0 and dinheiro==0):
            print('Você perdeu')      
else:
    print('Você perdeu')