import random
 
din_disponivel = 100
print (din_disponivel)
aposta = int(input("Qual sua aposta? "))
 
while din_disponivel > 0:
    if aposta == 0:
        break
    sorteio = random.randint(0, 36)
    if sorteio % 2 == 0:
        vdd_p_i = "p"
    else:
        vdd_p_i = "i"
    n_p = input("É número ou paridade? ")
    if n_p == "n":
        palpite = int(input("Qual o seu palpite? "))
        if sorteio == palpite:
            din_disponivel += (35 * aposta)
        else:
            din_disponivel -= aposta
    elif n_p == "p":
        p_i = input("É par ou impar? ")
        if vdd_p_i == p_i:
            din_disponivel += aposta
        else:
            din_disponivel -= aposta
    print (din_disponivel)
    aposta = int(input("Qual a sua nova aposta? "))