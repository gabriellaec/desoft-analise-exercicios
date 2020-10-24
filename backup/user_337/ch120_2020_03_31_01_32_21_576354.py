import random
din = 100
while din > 0:
    sorteado = random.randint(0,36)
    print(sorteado)
    print('seu dinheiro é',din)
    valor_apostado = int(input('Quanto você quer apostar? '))
    if valor_apostado == 0:
        break
    tipo = input('Sua aposta é um número (n) ou uma paridade (p)? ')
    if tipo == 'n':
        numero = int(input('Digite um numero de 1 a 36: '))
        if numero == sorteado:
            din = din + 35*valor_apostado
            print('Você ganhou a aposta')
        else:
            din = din - valor_apostado
            print('Você perdeu a aposta')
    if tipo == 'p':
        par_impar = input('Par (p) ou impar(i)? ')
        if par_impar == 'p':
            if sorteado%2 == 0:
                din = din + valor_apostado
                print('Você ganhou a aposta')
            else:
                din = din - valor_apostado
                print('Você perdeu a aposta')
        if par_impar == 'i':
            if sorteado%2 != 0:
                din = din + valor_apostado
                print('Você ganhou a aposta')
            else:
                din = din - valor_apostado    
                print('Você perdeu a aposta')