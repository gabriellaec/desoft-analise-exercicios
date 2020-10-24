import random
dinheiro = 100
n_sorteado = random.randint(0,36)

while dinheiro > 0:
    print(dinheiro)
    valor_da_aposta = int(input("Insira o valor da sua aposta: "))
    if valor_da_aposta <= 0:
        money = 0   
    else:
        tipo_de_aposta = input("Escolha o tipo de aposta: número (Digite 'n') ou paridade (Digite 'p')")
        if tipo_de_aposta == 'n':
            numero_apostado = int(input("Insira o número que você deseja apostar: "))
            if numero_apostado == n_sorteado:
                dinheiro += valor_da_aposta*35
                print(dinheiro)
            else:
                dinheiro -= valor_da_aposta
                print(dinheiro)
        if tipo_de_aposta == 'p':
            par_ou_impar = input("Insira se você quer apostar em par (Digite 'p') ou ímpar (Digite 'i')")
            if par_ou_impar == 'p':
                if n_sorteado % 2 == 0:
                    dinheiro += valor_da_aposta
                    print(dinheiro)
                else:
                    dinheiro -= valor_da_aposta
                    print(dinheiro)
            if par_ou_impar == 'i':
                if n_sorteado % 2 != 0:
                    dinheiro += valor_da_aposta
                    print(dinheiro)
                else:
                    dinheiro -= valor_da_aposta
                    print(dinheiro)