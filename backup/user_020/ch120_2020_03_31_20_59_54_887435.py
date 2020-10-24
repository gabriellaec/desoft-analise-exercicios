import random
dinheiro = 100
n_sorteado = random.randint(0,36)

while dinheiro > 0:
    valor_da_aposta = float(input("Insira o valor da sua aposta: "))
    if valor_da_aposta <= 0:
        break   
    tipo_de_aposta = input("Escolha o tipo de aposta: número (Digite 'n') ou paridade (Digite 'p')")
    if tipo_de_aposta == 'n':
        numero_apostado = int(input("Insira o número que você deseja apostar: "))
        if numero_apostado == n_sorteado:
            dinheiro += valor_da_aposta*35
            print("Você ganhou! Seu dinheiro agoraé: {0}" .format(dinheiro))
        else:
            dinheiro -= valor_da_aposta
            print("Você perdeu! Seu dinheiro agora é: {0}" .format(dinheiro))

    if tipo_de_aposta == 'p':
        par_ou_impar = input("Insira se você quer apostar em par (Digite 'p') ou ímpar (Digite 'i')")
        if par_ou_impar == 'p':
            par_apostado = int(input("Insira o número para que você deseja apostar: "))
            if n_sorteado % 2 == 0 and n_sorteado == par_apostado:
                dinheiro += valor_da_aposta
                print("Você acertou! Seu dinheiro agora é: {0}" .format(dinheiro))
            else:
                dinheiro -= valor_da_aposta
                print("Você perdeu! Seu dinheiro agora é: {0}" .format(dinheiro))
        if par_ou_impar == 'i':
            impar_apostado = int(input("Insira o número impar que você deseja apostar"))
            if n_sorteado % 2 != 0 and n_sorteado == impar_apostado:
                dinheiro += valor_da_aposta
                print("Você acertou! Seu dinheiro agora é: {0}" .format(dinheiro))
            else:
                dinheiro -= valor_da_aposta
                print("Você perdeu! Seu dinheiro agora é: {0}" .format(dinheiro))