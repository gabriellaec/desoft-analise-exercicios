import random

quantia=100
sorteio=random.randint(0,36)
while quantia>0:
    print("Sua quantia disponível é {0}".format(quantia))
    aposta=int(input("Qual o valor da aposta?"))
    if aposta==0:
        quantia=0
    else:
        noup=input("Número ou paridade")
        if  noup=="n":
            n=input("Digite um número entre 1 e 36:")
            if n==sorteio:
                quantia=quantia+35*aposta
            else:
                quantia=quantia-aposta
        if noup=='p':
            poui=input("Par ou impar?")
            if poui=="p"and sorteio%2==0:
                quantia=quantia +aposta
            elif poui=="i"and sorteio%2!=0:
                quantia= quantia+aposta
            else:
                quantia=quantia-aposta
            
    