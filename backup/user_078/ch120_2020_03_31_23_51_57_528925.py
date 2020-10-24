import random
dinheiro = 100
jogo = True

while jogo:
    if dinheiro>0:
        print ('Seu dinheiro:{0}'.format(dinheiro))
        a = int(input('Aposte um valor (se quiser sair, digite (out)): '))
        if a == 'out':
            jogo = False
        
        else:
            while a>dinheiro:
                a = int(input('Aposte um valor: '))
            n = random.randint (0, 36)
            b = input('Aposta em número (n) ou paridade (p)? ')
            while b!='n' and b!='p':
                b = input('Aposta em número (n) ou paridade (p)? ')
            if b == 'n':
                escolha = int(input('Escolha um número de 1 a 36: '))
                if escolha == n:
                    ganhar = True
                    lucro = 35*a
                else:
                    ganhar = False
                    lucro = -a
            else:
                escolha = input('Par (p) ou ímpar (i) (p/i)? ')
                while escolha != 'p' and escolha != 'i':
                    escolha (input('Par (p) ou ímpar (i)? '))
                if n%2==0:
                    vitoria = 'p'
                else:
                    vitoria = 'i'
                if escolha == vitoria:
                    ganhar = True
                    lucro = a
                else:
                    ganhar = False
                    lucro = -a
            print ('O número sorteado é {0}'.format(n))
            dinheiro = dinheiro+lucro
    else:
        jogo = False
    