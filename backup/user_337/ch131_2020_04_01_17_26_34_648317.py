import random
dado1 = random.randint(1, 10)
dado2 = random.randint(1, 10)
soma = dado1 + dado2
dinheiro = 10

#FASE DE DICAS
n1 = int(input('Fale um número: '))
n2 = int(input('Fale um número maior ou igual ao citado anteriormente: '))
if soma < n1:
    print('Soma menor')
elif soma > n2:
    print('Soma maior')
else:
    print('Soma no meio')

#FASE DE CHUTES
print('Você tem {} dinheiros disponíveis'.format(dinheiro))
n_chutes = int(input('Quantos chutes você quer comprar? Você só tem uma oportunidade de comprar chutes e cada um custa 1 dinheiro'))
dinheiro = dinheiro - n_chutes

while n_chutes > 0 :
    chute = int(input('Chute a soma dos dados lançados: '))
    n_chutes = n_chutes - 1
    if chute == soma:
        dinheiro = dinheiro + dinheiro * 5
        break

print("Você terminou o jogo com {} dinheiros".format(dinheiro))