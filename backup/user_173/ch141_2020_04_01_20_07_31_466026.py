print ('Bem vindo ao jogo, você começa com 1000 dinheiros.')
dinheiros = 1000
sorteio = random.randint (1,6)
sorteio2 = random.randint (1,6)
soma = (sorteio + sorteio2)

pergunta = input ('Você quer apostar? Responda "sim" se quiser e "não" se não quiser.)
if pergunta == 'n':
    print ('Obrigado pela participação e até a próxima!')

pergunta1 = int(input('Chute um número inicialmente. Vai custar 30 dinheiros'))
if pergunta1 = soma:
    dinheiros += +20

while pergunta1 != soma:
    pergunta 2 = input ('Você quer continuar apostando ou desiste? Responda "continuar" se quiser e "desistir" se não quiser.)
    if pergunta 2 == 'desistir':
        print ('Você voltará para o começo do jogo.')
        pergunta = input ('Você quer apostar? Responda "sim" se quiser e "não" se não quiser.)
    else:
        pergunta3 = int(input('Tente outro número. Vai te custar mais 20 dinheiros.')
            if pergunta3 = soma:
                dinheiros = 1000
            elif pergunta3 != soma:
                print ('A soma de um dos dados é {0}'.format(sorteio))
                pergunta 4 = input ('Você quer continuar apostando ou desiste? Responda "continuar" se quiser e "desistir" se não quiser. ')
                    if pergunta4 == 'desistir':
                        print ('Você voltará para o começo do jogo.')
                        pergunta = input ('Você quer apostar? Responda "sim" se quiser e "não" se não quiser.)
                    elif pergunta5 == 'continuar':
                        pergunta6 = int(input('Digite o valor do outro dado. Isso vai te custar mais 10 dinheiros'))
                        if pergunta6 = soma:
                            dinheiros = 990
                            print ('Você voltará para o começo do jogo.')
                            pergunta = input ('Você quer apostar? Responda "sim" se quiser e "não" se não quiser.)
                        else:
                            print ('Você errou e voltará para o começo do jogo.')
                        pergunta = input ('Você quer apostar? Responda "sim" se quiser e "não" se não quiser.)


