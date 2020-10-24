import random
fase = "Dicas"
money = 10
while money > 0:
    dado1 = random.randint(1,10)
    dado2 = random.randint(1,10)
    soma_dados = dado1+dado2
    if fase == "dicas":
        num1_jogador = int(input("Insira um número: "))
        num2_jogador = int(input("Insira um número maior ou igual ao número inserido anteriormente."))
        if soma_dados < num1_jogador:
            print("Soma menor")
        elif soma_dados > num2_jogador:
            print("Soma maior")
        else:
            print("Soma no meio")
        fase = "Chutes"
    else:
        print(money)
        chutes_comprados = int(input("Qtde chutes a comprar: "))
        money -= chutes_comprados
        while chutes_comprados > 0:
            chute_jogador = int(input("num de chute: "))
            if chute_jogador != soma_dados:
                chutes_comprados -= 1
                print("Seu chute esta errado")
            elif chute_jogador == soma_dados:
                money += money*5
                print("Seu chute esta correto")
                break
        if chutes_comprados == 0:
            print("Voce saiu do jogo com {0} dinheiros" .format(moneyu))
            break
print(soma_dados)