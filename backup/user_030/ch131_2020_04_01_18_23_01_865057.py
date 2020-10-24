import random

dinheiro = 10
while True:
    dado1 = random.randint(1, 10)
    dado2 = random.randint(1, 10)
    dica1 = int(input("Digite um número: "))
    dica2 = int(input("Digite um número maior ou igual ao anterior: "))
    valor_dados = dado1 + dado2
    valor_dicas = dica1 + dica2
    if valor_dicas < valor_dados:
        print("Soma menor")
    elif valor_dicas > valor_dados:
        print("Soma maior")
    else:
        print("Soma no meio")
    print("Você tem R$: ",dinheiro)
    chutes = int(input("Quantos chutes você quer comprar? "))
    dinheiro = dinheiro - chutes