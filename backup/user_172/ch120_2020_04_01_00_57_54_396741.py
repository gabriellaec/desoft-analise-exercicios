import random
dinheiro = 100
jogo=True
while jogo:
    if dinheiro>0:
        print ('você tem {0}'.format(dinheiro))
        valor_aposta= input('aposte um valor: ')
        if valor_aposta == 0:
            jogo=False
        else:
            while valor_aposta > dinheiro:
                valor_aposta = int(input('aposte um valor: ')
            r = randm.randint (0,36)
            qual_aposta = input('qual aposta?(p/n) ')
            while qual_aposta !='n' and qual_aposta!='p':
                qual_aposta = input('qual aposta?(p/n) ')
            if qual_aposta == 'n':
                chute = int(input('escolha um número de 1 a 36: ')
                if chute == r:
                    dinheiro = dinheiro + 35*valor_aposta
                    ganhar = True
                else:
                    dinheiro = dinheiro - valor_aposta
                    ganhar = False
            else:
                chute = input('par(p) ou impar(i)? ')
                while chute != 'p' and chute != 'i':
                    chute = input('par(p) ou impar(i)? ')
                if r%2==0:
                    v='p'
                else:
                    v='i'
                if chute==v:
                    ganhar=True
                    dinheiro = dinheiro + valor_aposta
                else:
                    ganhar=False
                    dinheiro = dinheiro - valor_aposta
            print ('O valor sorteado foi {0}'.format(r))
    else:
        jogo = False
        
   