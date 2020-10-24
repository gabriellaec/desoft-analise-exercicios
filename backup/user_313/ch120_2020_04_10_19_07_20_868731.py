import random

dinheiro = 100



while True:
    if dinheiro == 0:
        break
    dados = random.randint(0,36)
    print('Você tem {} dinheiros'.format(dinheiro))
    aposta = int(input('Qual sua aposta ? '))
    if aposta == 0:
        break
    else:
        pergunta = input('Sua aposta é um numero ou paridade ?')
        if pergunta == "n":
            resultado = int(input('Digite um numero de 1 a 36: '))
            if resultado == dados:
                dinheiro = dinheiro +(35*aposta)
                print('Voce ganhou')
            else:
                dinheiro = dinheiro - 10
                print('Voce Perdeu')
        
        if pergunta == "p":
            paridade = input('Par ou Impar ? ')
            if paridade == "p":
                if dados % 2 == 0:
                    dinheiro = dinheiro + aposta
                    print('Voce ganhou')
                else:
                    dinheiro = dinheiro - aposta
                    print('Voce Perdeu')
            if paridade == "i":
                if dados % 2 != 0:
                    dinheiro = dinheiro + aposta
                    print('Voce ganhou')
                else:
                    dinheiro = dinheiro - aposta
                    print('Voce Perdeu')