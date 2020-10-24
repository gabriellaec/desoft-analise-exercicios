import random
dinheiro=100
numero_aleatorio=random.randint(0, 36)
while dinheiro>0:
    print('Seu dinheiro disponível é: {}'.format(dinheiro))
    aposta=int(input('Aposte um valor: '))
    if aposta==0:
        break
    escolha=input('Digite n para apostar em um número ou p para apostar em paridade: ')
    if escolha=='n':
        numero=int(input('Digite um número de 1 a 36 para apostar: '))
        if numero==numero_aleatorio:
            dinheiro+=35*aposta
        else:
            dinheiro-=aposta
    elif escolha=='p':
        escolha_paridade=input('Digite p para Par ou i para ímpar: ')
        if escolha_paridade=='p':
            if numero_aleatorio%2==0:
                dinheiro+=aposta
            else:
                dinheiro-=aposta
        elif escolha_paridade=='i':
            if numero_aleatorio%2!=0:
                dinheiro+=aposta
            else:
                dinheiro-=aposta   