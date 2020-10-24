import random
primeiro_dado = random.randrange(10) + 1
segundo_dado = random.randrange(10) + 1
s = (primeiro_dado + segundo_dado)

dinheiro = 10

a = int(input('Me fale um número!'))
b = int(input('Me fale outro número maior ou igualao anterior!')
        
if s<a:
    print('Soma menor')
if s>b:
    print('Soma maior')
else:
    print('Soma no meio')

print('Você tem {0} dinheiro.'.format(dinheiro))
c = int(input('Quantos chutes você quer comprar? Cada chute custa 1 dinheiro e você só terá essa oportunidade de comprar')
dinheiro = dinheiro - c
        
while c>0:
    chute1 = int(input('Quanto deu a soma'))
    c = c - 1
if chute1 == s:
    dinheiro = (dinheiro + diheiro * 5)
    print('Você terminou o jogo com {0} dinheiro.'.format(dinheiro))
if chute1 != s:
    print('Você terminou o jogo com {0} dinheiro.'.format(dinheiro))