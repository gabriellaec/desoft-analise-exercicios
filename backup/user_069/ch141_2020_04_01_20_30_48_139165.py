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
            resp3 = input("Chute um número para a soma dos dados: ")
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            soma_dados = dado1 + dado2
            if resp3 == soma_dados:
                d = d + 30
            else:
                print(dado1)
                resp4 = input("Você quer continuar tentando ou quer desistir? ")
                if resp4 == "Desistir":
                    continue
                if resp4 == "Continuar":
                    resp5 = input("Chute um número para a soma dos dados: ")
                    dado1 = random.randint(1,6)
                    dado2 = random.randint(1,6)
                    soma_dados = dado1 + dado2