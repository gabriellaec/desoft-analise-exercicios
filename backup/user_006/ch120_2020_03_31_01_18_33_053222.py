import random

quantia=100

while quantia>0:
    sorteio=random.randint(0,36)
    print(quantia)
    aposta=int(input("Qual o valor da aposta?"))
    if aposta==0
        quantia=0
    elif aposta>quantia:
        
    else:
        noup=input("Número ou paridade?")
        if  noup=="n":
            numero=int(input("Digite um número entre 1 e 36:"))
            if numero==random.randint(0,36):
                quantia=quantia+(35*aposta)
                print(quantia)
            else:
                quantia=quantia-aposta
                print(quantia)
        else:
            poui=input("Par ou impar?")
            if poui=="p":
                if random.randint(0,36)%2==0:
                    quantia=quantia+aposta
                    print(quantia)
                    
                else:
                    quantia=quantia-aposta
            elif poui=="i":
                if random.randint(0,36)%2!=0:
                    quantia=quantia+aposta
                    print(quantia)
                    
                else:
                    quantia=quantia-aposta
            
    