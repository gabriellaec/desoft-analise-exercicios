import random
fase = "dicas"
dinheiro = 10
while dinheiro > 0:
    if fase == "dicas":
        soma_dados = random.randint(1,10) + random.randint(1,10)
        dica_1 = int(input("Insira um número: "))
        dica_2 = int(input("Insira um número maior ou igual ao número inserido anteriormente."))
        if soma_dados < dica_1:
            print("Soma menor")
        elif soma_dados > dica_2:
            print("Soma maior")
        else:
            print("Soma no meio")
        fase = "chutes"
    elif fase == "chutes":
        print(dinheiro)
        quantidade_de_chutes = int(input("Quantos chutes você deseja comprar? Obs: cada chute custa 1 dinheiro"))
        dinheiro -= quantidade_de_chutes
        while quantidade_de_chutes > 0:
            chute = int(input("Qual número você quer chutar?"))
            if chute != soma_dados:
                quantidade_de_chutes = quantidade_de_chutes - 1
                print("Você errou!")
            elif chute == soma_dados:
                dinheiro += dinheiro*5
                print("Você acertou!")
                break
        if quantidade_de_chutes == 0:
            print("Você terminou o jogo com {0} dinheiros" .format(dinheiro))
            break
print(soma_dados)