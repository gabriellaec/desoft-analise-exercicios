import random
caixa = 100
print(caixa)
aposta = int(input('Quanto deseja apostar? '))
while aposta > 0:
    a = random.randint(0, 36)
    tipo = input('Aposta em numero (n) ou paridade (p)')
    if tipo == 'n':
        numero = int(input('Escolha entre 1 e 36 '))
        if numero == a:
            caixa = caixa + 35*aposta
        else:
            caixa = caixa - aposta
    elif tipo == 'p':
        paridade = input('p ou i? ')
        if paridade == 'p':
            if a % 2 == 0:
                caixa = caixa + aposta
            else:
                caixa = caixa - aposta
        elif paridade == 'i':
            if a% 2 != 0:
                caixa = caixa + aposta
            else:
                caixa = caixa - aposta
    print('Você tem disponivel R$ {}'.format(caixa))
    if caixa > 0:
        aposta = int(input('Quanto deseja apostar? '))
    else:
        aposta = 0
        print('Não tem mais dinheiro')
