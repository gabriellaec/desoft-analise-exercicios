import random
din = 100
while din != 0:
    
    aposta = input("numero ou pariedade?")
    if aposta == "n":
        numerojogo = random.randint(1, 36)
        numero = int(input("fala numero de 1 a 36"))
        if numerojogo == numero: 
            din = din + 35*numero
            print(din)
        else:
            din = din - 10
            print(din)
    elif aposta == "p":
        numero2 = input("par  ou impar?")
        if numero2 == "p":
            numero2 = 2
        else:
            numero2 = 1       
                   
        parimpar = random.randint(1, 2)
        if numero2 == parimpar:
            din = din + 10
            print(din)
        else: 
            din -= 10
            print (din)
    else:
        break
        print(din)
                     
                     
                     
    