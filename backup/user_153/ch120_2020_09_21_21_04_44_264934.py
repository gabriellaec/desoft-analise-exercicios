from random import randint

dinheiro = 100
while dinheiro > 0:
    print("Dinheiro disponivel: ", dinheiro)
    valor_aposta = int(input("Qual o valor da aposta: "))
    while valor_aposta > dinheiro:
        valor_aposta = int(input("Dinheiro insuficiente!\nQual o valor da aposta: "))
    print("Valor aposta: {}".format(valor_aposta))
    if valor_aposta == 0:
        print("Jogo finalizado")
        break
    tipo_de_jogo = input("Qual o tipo de aposta? (paridade: p/numero: n) ")
    print("Tipo de jogo:",tipo_de_jogo)
    if tipo_de_jogo == 'p':
        paridade = input("Deseja aposta em par ou impar? (p/i) ")
        print("Paridade ", paridade)
        while paridade != 'p' and paridade != 'i':
            paridade = input("Selecao invalida!\nDeseja aposta em par ou impar? (p/i) ")
        sorteio = randint(0,36)
        print("Número sorteado é ", sorteio)
        if sorteio%2==0 and paridade == 'p':
            dinheiro += valor_aposta
            print("Ganhou. Novo saldo igual a {}".format(dinheiro))
        elif sorteio%2==1 and paridade == 'i':
            dinheiro += valor_aposta
            print("Ganhou. Novo saldo igual a {}".format(dinheiro))
        else:
            dinheiro -= valor_aposta
            print("Perdeu. Novo saldo igual a {}".format(dinheiro))
    elif tipo_de_jogo == 'n':
        numero_apostado = int(input("Em qual número deseja apostar? (1 a 36)"))
        while numero_apostado > 36 or numero_apostado < 1:
            numero_apostado = int(input("Número invalido!\nEm qual número deseja apostar? (1 a 36)"))
        sorteio = randint(0,36)
        print("Número sorteado é ", sorteio)
        if numero_apostado == sorteio:
            dinheiro += 35*valor_aposta
            print("Ganhou. Novo saldo igual a {}".format(dinheiro))
        else:
            dinheiro -= valor_aposta
            print("Perdeu. Novo saldo igual a {}".format(dinheiro))
    else:
        print("Tipo invalido. Recomeçando.")

