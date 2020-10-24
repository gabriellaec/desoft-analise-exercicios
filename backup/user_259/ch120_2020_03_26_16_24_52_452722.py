import random
din = 100
run = True
while run:
    print("Dinheiro disponível: ", din)
    ap = int(input("Aposte um valor: "))
    if ap == 0:
        run = False
    else:
        sorteio = random.randint(0,36)
        par_ou_impar = input("Você vai apostar em par(p), ímpar(i) ou outro(n)? ")
        if par_ou_impar == 'n':
            um_a_trinseis = int(input("Digite um número de 1 a 36: "))
            if um_a_trinseis == sorteio:
                din+=ap*35
                print("Você ganhou!")
                
            else:
                din-=ap
                print("Você perdeu!")
                
        if par_ou_impar == 'p' or par_ou_impar == 'i':
            if sorteio%2 == 0:
                sorteio = 'p'
            else:
                sorteio = 'i'
            if par_ou_impar == sorteio:
                din+=ap
            else:
                din-=ap
            
        if par_ou_impar == 'i':
            if sorteio%2 != 0:
                sorteio = 'i'
            else:
                sorteio = 'p'
            if par_ou_impar == sorteio:
                din+=ap
            else:
                din-=ap