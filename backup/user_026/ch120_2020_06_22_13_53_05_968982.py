import random
dinheiro=100
valor = 1
while dinheiro!=0 and valor !=0:
    print("seu saldo é de {0} reais".format(dinheiro))
    valor = int(input("Qual valor deseja apostar? ")
    if valor != 0 :
    	aposta = int(input("O valor da sua aposta é um numero impar(i) ou par(p)? ")
        numero_aleatorio = random.randint(0,36)
        if aposta == "i":
             numero = int(input("digite aqui um numero de 1 a 36: "))
             if numero == numero_aleatorio:
                     dinheiro+= valor*35
                     print("seu saldo é de: {0} reais".format(dinheiro))
            else:
                dinheiro-= valor
                print("seu saldo é de: {0} reais".format(dinheiro))
        elif aposta == "p":
            par_impar= input("escolha se o número será par ou ímpar (p/i): ")
            if numero_aleatorio%2 == 0:
                if par_impar=="p":
                     dinheiro += valor
                     print("seu saldo é de: {0} reais".format(dinheiro))
                elif par_impar == "i":
                    dinheiro-=valor
                    print("seu saldo é de: {0} reais".format(dinheiro))
            elif numero_aleatorio%2 != 0:
                     if par_impar == "i":
                        dinheiro+=aposta
                        print("seu saldo é de: {0} reais".format(dinheiro))
                     else:
                         dinheiro -= valor
                         print("seu saldo é de: {0} reais".format(dinheiro))
print("Game Over")

