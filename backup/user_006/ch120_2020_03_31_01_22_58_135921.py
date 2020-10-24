import random

quantia = 100

while quantia > 0:
    print("Seu crédito: R$ {0}" .format(quantia))
    aposta= int(input("Digite o valor da aposta:"))
    if aposta <= 0:
        quantia = 0
    else:
        tipo = input("Digite o tipo da aposta:")   
        if tipo == 'n':
            numero = int(input('Número de 1 a 36:'))
            if numero == random.randint(0,36):
                quantia += 35*aposta
                print(quantia)
            else:
                quantia -=aposta
                print(quantia)
        elif tipo == 'p':
            poui = input("Digite o tipo da aposta:")  
            if poui == 'p':
                if random.randint(0,36) % 2 == 0:
                    quantia += aposta
                    print(quantia)
                else:
                    quantia -= aposta
                    print(quantia)
            elif poui == 'i':
                if random.randint(0,36) % 2 != 0:
                    quantia += aposta
                    print(quantia)
                else:
                    quantia -= aposta
                    print(quantia)