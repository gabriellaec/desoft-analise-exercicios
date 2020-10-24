from random import randint
dinheiros = 1000
while (dinheiros>0):
    pergunta1 = input("Você quer apostar?: (Digite sim ou não)")
    if pergunta == "não":
    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
    break
else:
    Dado1 = random.randint(1,6)
    Dado2 = random.randint(1,6)
    soma_dos_dados = Dado1 + Dado2
    chute1=input("Qual o seu chute para o valor da soma dos dados?: ")
    dinheiros = dinheiros - 30
    if chute == soma_dos_dados:
        dinheiros = dinheiros + 50
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
    else:
        pergunta2= input("Você deseja continuar ou vai desistir?: (Digite continuar ou desistir)")
        if pergunta5 == "desistir":
        print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
        continue
        else:
            chute2 = input("Tente novamente: ")
            dinheiros = dinheiros - 20
            if chute2 == soma_dos_dados:
                dinheiros= dinheiros+50
            print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
            else:
                print(Dado1)
                pergunta3= input("Você deseja continuar ou vai desistir?: (Digite continuar ou desistir)")
                if pergunta3 == "desistir":
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                    continue
                if pergunta3 == "continuar":
                    chute3 = input("Tente novamente: ")
                    dinheiros = dinheiros - 10
                    if chute3 == soma_dos_dados:
                    print('Você terminou a partida com {0} dinheiros'.format(dinheiros))
                    dinheiros = dinheiros + 50
                    continue
    