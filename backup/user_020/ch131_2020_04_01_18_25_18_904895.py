import random
fase = "dicas"
dinheiro = 10
while dinheiro > 0:
    if fase == "dicas":
        soma_dados = random.randint(1,10) + random.randint(1,10)
        dica_1 = int(input("Insira um número: "))
        dica_2 = int(input("Insira um número maior ou igual ao número inserido anteriormente: "))
        if dica_1 > soma_dados:
            print("Soma menor")
        elif dica_2 < soma_dados:
            print("Soma maior")
        else:
            print("Soma no meio")
        fase = "chutes"
    else:
        print(dinheiro)
        quantidadedechutes = int(input("Quantos chutes você deseja comprar? Obs: cada chute custa 1 dinheiro "))
        dinheiro -= quantidadedechutes
        while quantidadedechutes > 0:
            chute = int(input("Qual número você quer chutar?"))
            if chute != soma_dados:
                quantidadedechutes = quantidadedechutes - 1
                print("Você errou!")
            elif chute == soma_dados:
                dinheiro += dinheiro*5
                print("Você acertou!")
                break
        if quantidadedechutes == 0:
            print("Você terminou o jogo com {0} dinheiros" .format(dinheiro))
            break
