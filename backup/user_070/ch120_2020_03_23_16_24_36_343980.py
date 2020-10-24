import random
cart = 100
jogo = True
while jogo:
    if cart>0:
        print('Seu dinheiro: {0}'.format(cart))
        a = int(input('Aposte um valor(se quiser sair, digite (0)): '))
        if a==0:
            jogo = False
        else:
            while a>cart:
                a = int(input('Aposte um valor: '))
            n = random.randint(0,36)
            b = input('Aposta em número (n) ou paridade (p)? ')
            while b!='n' and b!='p':
                b = input('Aposta em número (n) ou paridade (p)? ')
            if b=='n':
                choice = int(input('Escolha um número de 1 a 36: '))
                if choice == n:
                    ganhar = True
                    lucro = 35*a
                else:
                    ganhar = False
                    lucro = -a
            else:
                choice = input('Par (p) ou ímpar (i)? ')
                while choice != 'p' and choice != 'i':
                    choice = input('Par (p) ou ímpar (i)? ')
                if n%2==0:
                    v='p'
                else:
                    v='i'
                if choice==v:
                    ganhar = True
                    lucro = a
                else:
                    ganhar = False
                    lucro = -a
            print('O número sorteado é {0}'.format(n))
            cart += lucro
    else:
        jogo = False