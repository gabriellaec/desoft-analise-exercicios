import random
dinheiro = 100

while dinheiro > 0 :
    sorteio = random.randint (0, 36)
    print('dinheiro disponivel: {0}' .format(dinheiro))
    aposta = int(input('quanto quer perder? ' ))
    if aposta > dinheiro:
        print ('voce está louco')
    if aposta == 0 :
        break
    metodo = input('como quer apostar?(n, p) ')
    if metodo == 'n' :
        numerozin = int(input ('digite de 1 a 36: '))
        if numerozin == sorteio:
            dinheiro = aposta*35 + dinheiro
        else:
            dinheiro = dinheiro - aposta
    elif metodo == 'p':
        numerozin = input ('p ou i? ')
        if numerozin == 'p':
            if sorteio%2 == 0:
                dinheiro = dinheiro + aposta
                print('voce ganho cagado')
            else:
                dinheiro = dinheiro - aposta
                print('se deu mal')
        elif numerozin == 'i':
            if sorteio%2 != 0:
                dinheiro = dinheiro + aposta
                print('se ganho, mas duvido aposta do outro jeito')
            else:
                dinheiro = dinheiro - aposta
                print('perder rapaiz')
print('falou otario')  