import random
dinheiro = 100

while dinheiro > 0:
    print("Suas fichas: {0}" .format(dinheiro))    
    aposta= int(input('De quanto é sua aposta? '))
    if aposta == 0:
        break
    elif aposta != 0 :
        numero_escolhido = random.randint(0, 36)
        pergunta= input('Aposta em numero ou paridade? (n/p)')
        
        if pergunta == 'n':
            a = int(input('Digite um número de 1 a 36: '))
            if a == numero_escolhido:
                dinheiro += 35*aposta
            else:
                dinheiro -= aposta
        else:
            b = input("par ou ímpar? (p/i)")
            if b == 'p':
                if numero_escolhido % 2 == 0:
                    dinheiro += aposta
                else:
                    dinheiro -= aposta
            if b == 'i':
                if numero_escolhido % 2 != 0:
                    dinheiro += aposta 
                else:
                    dinheiro -= aposta