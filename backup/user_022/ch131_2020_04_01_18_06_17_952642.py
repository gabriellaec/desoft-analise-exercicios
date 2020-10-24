import random
dinheiros=10
while True:
    dado1 = randm.randint(1, 10)
    dado2 = randm.randint(1, 10)
    resulta_dodado = dado1+dado2
    dica1 = int(input("Digite um número inteiro: "))
    dica2 = int(input("Digite um número inteiro maior ou igual ao anterior: "))
    resultado_dica = dica1+dica2
    if resultado_dica < resulatdo_dado:
        print("Soma menor")
    elif resultado_dica > resultado_dado:
        print("Soma maior")
    else:
        print("Soma no meio")
    print("Você tem R$:",dinheiro)
    numero_chutes = int(input("Quantos chutes você quer comprar? "))
    dinheiro -= numero_chutes
    while nchutes>0:
        print("Você tem ", numero_chutes, "chutes.")
        numero_chutes-=1
        chute=int(input("Adivinhe a soma: "))
        if chute == resultado_dado:
            dinheiros*=5
            break
        print("Errou!")
    if numero_chutes==0:
        print("Você terminou o jogo com R$", dinheiros)
        break