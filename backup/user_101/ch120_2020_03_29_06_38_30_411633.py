import random

din_disponível = 100
print (din_disponivel)
aposta = int(input("Qual sua aposta? ")

while aposta > 0:
    sorteio = random.randint(1, 37)
    if sorteio % 2 == 0:
        vdd_p_i = "p"
    else:
        vdd_p_i = "i"

    n_p = input("É número ou paridade? ")
    if n_p == "n":
        palpite = int(input("Qual o seu palpite? "))
        if sorteio == palpite:
            din_disponível += (35 * aposta)
        else:
            din_disponível -= aposta

    elif n_p == "p":
        p_i = input("É par ou impar? ")
        if vdd_p_i == p_i:
            din_disponível += aposta
        else:
            din_disponível -= aposta
        
    print (din_disponivel)
    aposta = int(input("Qual a sua nova aposta? ")
             