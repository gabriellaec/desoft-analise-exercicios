import random
d=100
while d>0:
    r=random.randint(0,36)
    print(f"Dinheiro disponível: {d}")
    aposta=int(input("Quanto você deseja apostar? "))
    if aposta==0:
        break
    elif aposta>d:
        print("Você não tem dinheiro suficiente")
    else:
        Tipo=input("Qual o tipo de aposta? Número ou Paridade? ")
        if Tipo=="Número":
            n=int(input("Escolha um número de 0 a 36: "))
        if n==r:
            	d=d+aposta*35
        else:
            	d=d-aposta
        if Tipo=="Paridade":
            p=input("Par ou ímpar? ")
        if r%2==0:
            r="Par"
        else:
            r="Ímpar"
        if p==r:
            d=d+aposta
        else:
            d=d-aposta
			else:
                r="Ímpar"
			if r==p:
                d=d+aposta
            else:
                d=d-aposta
            

                
            
            

       
            
            
               
      