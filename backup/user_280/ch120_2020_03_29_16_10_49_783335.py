import sys
import random
caixa = 100
print('Você tem {} dinheiros'.format(caixa))
aposta = input('Aposte uma valor: ')
if aposta == 0:
    sys.exit
else:
    tipo = input('Núméro ou paridade: ')
    sorteado = random.randint(0,36)
    if tipo == n:
        jogo = input('Digite um número de 1 a 36: ')
        if jogo == sorteado:
            caixa += 35*aposta
            print('Você ganhou e tem {} dinheiros'.format(caixa))
        else: 
            caixa -= 10
            print('Você perdeu e tem {} dinheiros'.format(caixa))
    if tipo == p:
        if sorteado%2 == 0:
         	resultado = p
        else:
            resultado = i
            jogo = input('Digite uma paridade: ')
            if jogo == resultado:
                caixa += 10
                print('Você ganhou e tem {} dinheiros'.format(caixa))
            else:
                caixa -= 10
                print('Você perdeu e tem {} dinheiros'.format(caixa))