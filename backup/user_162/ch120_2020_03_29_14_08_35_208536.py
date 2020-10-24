import random

total = 100

while total > 0:
    print("Voce tem {} reais.".format(total))
    aposta = int(input("Quanto quer apostar? "))
    opcao = input("Escolha numero(n) ou paridade(p): ")
    roleta = random.randint(0,36)
    #debug
    print(roleta)
    #debug
    if aposta == 0 or aposta > total:
        print("Voce nao sabe apostar!")
        break
    
    elif opcao == "n":
        num = int(input("Escolha um numero de 1 a 36: "))
        if num == roleta:
            total += 35*aposta
        else:
            total -= aposta
    else:
        parimp = input("Escolha entre par(p) ou impar(i): ")
        if roleta%2 == 0 and parimp == "p":
            total+=aposta
        elif roleta%2 == 1 and parimp == "i":
            total+=aposta
        else:
            total-=aposta
else:
    print("Voce faliu!!!")