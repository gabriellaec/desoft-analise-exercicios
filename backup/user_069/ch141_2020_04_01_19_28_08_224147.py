import random
d = 1000
jogando = True
while jogando:
    resp = input("Você quer apostar? ")
    if resp == "não":
        break
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    soma_dados = dado1 + dado2
    resp1 = input("Chute um número para a soma dos dados: ")
    if resp1 == soma_dados:
        d = d + 20
        continue
    if resp1 != soma_dados:
        d = d - 60
        resp2 = input("Você quer continuar tentando ou quer desistir? ")
        if resp2 == "Desistir":
            continue
        else: