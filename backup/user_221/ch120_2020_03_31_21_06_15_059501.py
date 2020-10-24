import random
caixa = 100
print(caixa)
aposta = int(input('Quanto deseja apostar? '))
while aposta > 0:
    a = random.randint(0, 36)
    tipo = input('Aposta em numero (n) ou paridade (p/i) ')
    if tipo == 'n':
        numero = int(input('Escolha entre 1 e 36 '))
        if numero == a:
            caixa = caixa + 35*aposta
        else:
            caixa = caixa - aposta
    elif tipo == 'p':
        if a % 2 == 0:
            caixa = caixa + aposta
        else:
            caixa = caixa - aposta
    elif tipo == 'i':
        if a% 2 != 0:
            caixa = caixa + aposta
        else:
            caixa = caixa - aposta
    
    if caixa > 0:
        aposta = int(input('Quanto deseja apostar? '))
    else:
        aposta = 0
        