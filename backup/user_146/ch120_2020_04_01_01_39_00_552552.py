import random
dinheiro = 100
while dinheiro > 0:
    print(dinheiro)
    aposta  = float(input('Quanto voce deseja apostar? '))
    if aposta <= 0 or aposta > dinheiro:
        break
    else:
        tipo_aposta = input('Voce deseja apostar em um numero (n) ou disparidade (p)? ')
    
    if tipo_aposta == 'n':
        escolha_numero = int(input('Escolha em numero de 1 a 36 '))
        numero_sorteado = random.randint(1,36)
        if escolha_numero == numero_sorteado:
           dinheiro = aposta *35
           print(dinheiro)
        else:
            dinheiro -= aposta
            print(dinheiro)
            break
    
    if tipo_aposta == 'p':
        escolha_par_impar = input('Voce deseja apostar em um numero par (p) ou impar (i)? ')
        if escolha_par_impar == 'p':
            numeros_par = random.randint(1,36)
            if numeros_par %2 == 0:
                dinheiro = dinheiro + aposta
                print(dinheiro)
            else:
                dinheiro -= aposta
                print(dinheiro)
                break
        
        if escolha_par_impar == 'i':
            numeros_impar = random.randint(1,36)
            if numeros_impar %2 != 0:
                dinheiro += aposta
                print(dinheiro)
            else:
                dinheiro -= aposta
                print(dinheiro)
                break