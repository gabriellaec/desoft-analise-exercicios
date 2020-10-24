import random
a = random.randint(1,10)
b = random.randint(1,10)
c = a + b
j = 10
while j != 0 or c != (x+y):
    x = int(input('Digite o primeiro número: '))
    y = int(input('Digite o segundo número: '))
    if (x+y) <c:
        j = j - 1
        print("Soma menor")
    elif (x+y)>c:
        j = j - 1
        print('Soma maior')
    else:
        j = j * 5
        print("Soma no meio")
        print("Você terminou o jogo com {0} dinheiros".format(j))
