import random

grana = 10
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
soma_dados = dado1 + dado2 + dado3

# FASE DE DICAS
def fase_de_dicas(dinheiros):
    if dinheiros > 0:
        print('Você tem {} dinheiro(s).'.format(dinheiros))
        resposta1 = input('Você aceita uma dica? Custa 1 dinheiro. (sim/nao)')
        if resposta1 == 'sim':
            dinheiros = dinheiros - 1
            chute1 = input('Digite seu primeiro chute: ')
            chute2 = input('Digite seu segundo chute: ')
            chute3 = input('Digite seu terceiro chute: ')
            if chute1 == soma_dados or chute2 == soma_dados or chute3 == soma_dados:
                print('A resposta está entre esses números')
        elif resposta1 == 'nao':
            print('OK! Vamos aos chutes.')
    else:
        print('Que pena, você não tem mais dinheiro')
            
# FASE DE CHUTES

def fase_de_chutes(dinheiros):
    while dinheiros > 0:
        print('Você tem {} dinheiro(s).'.format(dinheiros))
        chute_final = input('Qual é o valor da soma?')
        if chute_final == soma_dados:
            premio = dinheiros * 3
            print('Parabéns! Você ganhou o jogo com {} dinheiros.'.format(premio))
        else:
            dinheiros = dinheiros - 1
            print('Não é essa a resposta. Você tem agora {} dinheiro(s).'.format(dinheiros))
            
# RODANDO O JOGO
            
fase_de_dicas(grana)
fase_de_chutes(grana)