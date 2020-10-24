import random
Encerrar = False
Dinheiros = 1000
while Encerrar == False:
    a = input("Quer apostar? ")
    if a == 'Não':
        print("Encerrar")
        Encerrar = True
    else:
        Desistir = False
        while Desistir == False:
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            soma = dado1 + dado2
            b = input("Aposta (custa 30 Dinheiros): ")
            Dinheiros = Dinheiros - 30
            if b == soma:
                print("Você ganhou 50 Dinheiros!")
                Dinheiros = Dinheiros + 50
                print("Você tem {0} Dinheiros.".format(Dinheiros))
            else:
                print("Você tem {0} Dinheiros.".format(Dinheiros))
                c = input("Deseja 'desistir' ou 'continuar'? ")
                if c == 'desistir':
                    Desistir = True
                else:
                    Desistir = False
                    d = input("Digite sua  nova aposta (custa 20 Dinheiros):")
                    Dinheiros = Dinheiros - 20
                    if d == soma:
                        print("Você ganhou 50 Dinheiros!")
                        Dinheiros = Dinheiros + 50
                        print("Você tem {0} Dinheiros.".format(Dinheiros))
                    else:
                        print("Dado 1: {0}".format(dado1))
                        print("Você tem {0} Dinheiros.".format(Dinheiros))
                        e = input("Deseja 'desistir' ou 'continuar'? ")
                        if e == 'desistir':
                            Desistir = True
                        else:
                            f = input("Digite sua  nova aposta (custa 10 Dinheiros):")
                            Dinheiros = Dinheiros - 10
                            if f == soma:
                                print("Você ganhou 50 Dinheiros!")
                                Dinheiros = Dinheiros + 50
                                print("Você tem {0} Dinheiros.".format(Dinheiros))
                                Desistir = True
                            else:
                                print("Você perdeu! Você tem {0} Dinheiros.".format(Dinheiros))
                                Desistir = True
print('Você terminou a partida com {0} Dinheiros.'.format(Dinheiros))