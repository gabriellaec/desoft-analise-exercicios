import random

quantia=100
perdeu=True
while quantia>0 and perdeu:
    sorteio=random.randint(0,36)
    print("Sua quantia disponível é {0}".format(quantia))
    aposta=int(input("Qual o valor da aposta?"))
    if aposta==0:
        quantia=0
    else:
        noup=input("Número ou paridade")
        if  noup=="n":
            numero=int(input("Digite um número entre 1 e 36:"))
            if numero==sorteio:
                quantia=quantia+(35*aposta)
                print(quantia)
                perdeu=False
            else:
                quantia=quantia-aposta
                print(quantia)
        else:
            poui=input("Par ou impar?")
            if poui=="p":
                if sorteio%2==0:
                    quantia=quantia +aposta
                    print(quantia)
                    perdeu=False
                else:
                    quantia=quantia-aposta
            else:
                if sorteio%2==0:
                    quantia= quantia-aposta
                else:
                    quantia=quantia+aposta
                    print(quantia)
                    perdeu=False
            
    