import random
din = 100
print("Dinheiro disponível: ", din)
run = True
while run:
    ap = int(input("Aposte um valor: "))
    if ap == 0:
        run = False
    else:
        sorteio = random.randint(1,36)
        par_ou_impar = input("Você vai apostar em par(p), ímpar(i) ou outro(n)? ")
        if par_ou_impar == 'n':
            um_a_trinseis = int(input("Digite um número de 1 a 36: "))
            if um_a_trinseis == numero:
                din+=ap*35
                print("Você ganhou!")
                print("Dinheiro disponível: ", din)
            else:
                din-=ap
                print("Você perdeu!")
                print("Dinheiro disponível: ", din)
        if par_ou_impar == 'p':
            if sorteio%2 == 0:
                din+=ap
                print("Você ganhou!")
                print("Dinheiro disponível: ", din)
            else:
                din-=ap
                print("Você perdeu!")
                print("Dinheiro disponível: ", din)
        if par_ou_impar == 'i':
            if sorteio%2 == 0:
                din-=ap
                print("Você perdeu!")
                print("Dinheiro disponível: ", din)
            else:
                din+=ap
                print("Você ganhou!")
                print("Dinheiro disponível: ", din)