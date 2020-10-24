dinheiro = 1000

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

soma_dados = dado1 + dado2

x = input("Você quer apostar?")

while x != "não" and dinheiro > 0:
    chute_inicial = int(input("Chute um valor entre 2 e 12!. Custará 30 dinheiros"))
    dinheiro -= 30
    if chute_inicial == soma_dados:
        dinheiro += 50
    elif chute_inicial != soma_dados:
        chute_2 = input("Você errou!. Quer tentar denovo?")
        if chute_2 == "desitir":
            break
        elif chute_2 != "desitir":
            chute_3 = int(input("Digite seu chute:"))
            dinheiro -= 20
            if chute_3 == soma_dados:
                dinheiro += 50
                break
            elif chute_3 != soma_dados:
                chute_4 = input("O valor de um dado é {0}. Você quer continuar tentando?(continuar ou desistir)".format(dado1))
                if chute_4 == "desistir":
                    break
                elif chute_4 == "continuar":
                    dinheiro -= 10
                    chute_5 = int(input("Digite seu chute:"))
                    if chute_5 == soma_dados:
                        dinheiro +=50
                        break

print("Você terminou a partida com {0} dinheiros.".format(dinheiro))