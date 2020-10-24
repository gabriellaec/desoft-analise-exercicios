from random import randint
dinheiro=10
jogando = True
while jogando:
    jogada1=randint(2, 10)
    jogada2=randint(2, 10)
    valor=jogada1+jogada2
    dica1=int(input("Digite um número: "))
    dica2=int(input("Digite um número maior do que o anterior: "))
    valordica=dica1+dica2
    if valordica<valor:
        print("Soma menor")
    elif valordica>valor:
        print("Soma maior")
    else:
        print("Soma no meio")
    print("Você tem R$:",dinheiro)
    num_tentativas=int(input("Quantos chutes você quer comprar? "))
    dinheiro-=num_tentativas
    while num_tentativas>0:
        print("Você tem ", num_tentativas, "chutes.")
        num_tentativas-=1
        chute=int(input("Adivinhe a soma: "))
        if chute==valor:
            dinheiro*=5
            break
        print("Errou!")
    if num_tentativas==0:
        print("Você terminou o jogo com R$", dinheiro)
        break
    
    
    