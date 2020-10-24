import random

ficha = 100
programa = True
tipo = 0
escolha = 0
sorteio = 0
resultado = 0

while programa:
    print('Essa são suas fichas:',ficha)
    if ficha == 0:
        programa = False

    else:
            
        print('Essa são suas fichas:',ficha)
        aposta = int(input('Qual o valor você deseja aposta:'))

        if aposta == 0 or aposta > ficha :
            programa = False

        else:
            tipo = input('Sua aposta é uma paridade(p) ou nenhum(n):')

            if tipo == 'n':
                escolha = int(input('Digite um numero de 0 a 36:'))
                sorteio = random.randint(0,36)

                if sorteio == escolha:
                    print('Você ganhou')
                    ficha = ficha + (aposta*35)
                
                else:
                    print('Você perdeu')
                    ficha = ficha - aposta

            if tipo == 'p':
                sorteio = random.randint(0,36)
                tipo2 = input('Par(p) ou impar(i):')

                if sorteio % 2 == 0:
                    resultado ==  'p'

                else:
                    resultado == 'i'

                if tipo2 == resultado:
                    print('Você Ganhou')
                    ficha = ficha + aposta

                else:
                    print('Voce Perdeu')
                    ficha = ficha - aposta








                
