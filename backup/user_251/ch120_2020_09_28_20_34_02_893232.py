import random
jogo_valido = True
dinheiro = 100
print("Você tem 100 dólares para apostar")
while dinheiro > 0 and jogo_valido:
    valor_aposta = float(input("Qual o valor que deseja apostar?: "))
    tipo_aposta = input("Qual o tipo de aposta: numero, par ou impar? ")
    if valor_aposta == 0:
        jogo_valido = False
    if tipo_aposta == "numero":
        resultado = random.randint(1, 37)
        numero_apostado = int(input("escolha um número de 1 a 36 "))
        if resultado == numero_apostado:
            dinheiro += 35*(valor_aposta)
            print("O numero foi {0}".format(resultado))
            print("Voce tem {0} dólares para apostar".format(dinheiro))
        elif resultado != numero_apostado:
            dinheiro = dinheiro - valor_aposta
            print("O numero foi {0}".format(resultado))
            print("Voce tem {0} dólares para apostar".format(dinheiro))
    elif tipo_aposta == "par":
        resultado = random.randint(1, 37)
        if resultado % 2 == 0:
            dinheiro += 2*(valor_aposta)
            print("O numero foi {0}".format(resultado))
            print("Você ganhou {0} dólares!".format(2*valor_aposta))
            print("Voce tem {0} dólares para apostar".format(dinheiro))
        else:
            dinheiro = (dinheiro - valor_aposta)
            print("O numero foi {0}".format(resultado))
            print("Você perdeu {0} dólares.".format(valor_aposta))
            print("Voce tem {0} dólares para apostar".format(dinheiro))
    elif tipo_aposta == "impar" or "ímpar":
        resultado = random.randint(1, 37)
        if resultado % 2 != 0:
            dinheiro += 2*(valor_aposta)
            print("O numero foi {0}".format(resultado))
            print("Voce tem {0} dólares para apostar".format(dinheiro))
        else:
            dinheiro = dinheiro - valor_aposta
            print("O numero foi {0}".format(resultado))
            print("Voce tem {0} dólares para apostar".format(dinheiro))

print("O jogo acabou!")
