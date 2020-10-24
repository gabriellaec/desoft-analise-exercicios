import random
caixa = 100
print('Você tem {} dinheiros'.format(caixa))
aposta = int(input('Aposte uma valor: '))
if aposta != 0:
    tipo = input('Número ou paridade: ')
    sorteado = random.randint(0,36)
    if tipo == 'n':
        jogo = input('Digite um número de 1 a 36: ')
        if jogo == sorteado:
            caixa += 35*aposta
            print('Você ganhou e tem {} dinheiros'.format(caixa))
        else: 
            caixa -= aposta
            print('Você perdeu e tem {} dinheiros'.format(caixa))
    if tipo == 'p':
        jogo = input('Digite uma paridade: ')
        if sorteado%2 == 0:
         	resultado = 'p'
        else:
            resultado = 'i'
        if jogo == resultado:
            caixa += aposta
            print('Você ganhou e tem {} dinheiros'.format(caixa))
        else:
            caixa -= aposta
            print('Você perdeu e tem {} dinheiros'.format(caixa))
else:
    print('Tente outra vez')