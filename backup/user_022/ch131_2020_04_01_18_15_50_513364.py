from random import randint
dinheiros=10
while True:
    dado1 = random.randint(1, 10)
    dado2 = random.randint(1, 10)
    resultado_do_dado = dado1+dado2
    dica1 = int(input("Digite um número inteiro: "))
    dica2 = int(input("Digite um número inteiro maior ou igual ao anterior: "))
    resultado_dica = dica1+dica2
    if resultado_dica < resultado_do_dado:
        print("Soma menor")
    elif resultado_dica > resultado_do_dado:
        print("Soma maior")
    else:
        print("Soma no meio")
    print("Você tem R$:",dinheiro)
    numero_chutes = int(input("Quantos chutes você quer comprar? "))
    dinheiros -= numero_chutes
    while numero_chutes>0:
        print("Você tem ", numero_chutes, "chutes")
        numero_chutes-=1
        chute=int(input("Adivinhe a soma: "))
        if chute == resultado_do_dado:
            dinheiros*=5
            break
        print("Errou!")
    if numero_chutes==0:
        print("Você terminou o jogo com R$", dinheiros)
        break