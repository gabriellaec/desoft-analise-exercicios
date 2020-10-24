import random
din = 100
par=-1
num=-1
x=-1
while din>0 and x!=0:
    print('Disponível R${0}'.format(din))
    x = int(input("Quanto você irá apostar: "))
    if x==0:
        print("Você Parou!") 
    else:
        aposta = input("Sua aposta é em um número ou paridade(n/p):  ")
        if aposta=="n":
            num = int(input("Digite um número de 1 a 36: "))
        elif aposta=="p":
            par = input("Escolha entre par ou ímpar(p/i): ")
        else:
            print("Apostas em apenas número e paridade!")
        sorteio = random.randint(0,36)
        print("O número sorteado foi {0}".format(sorteio))
        m=sorteio%2
        if sorteio == num and aposta == "n":
            din= din + x*35
        elif m==0 and par=="p" and aposta=="p":
            din = din + x
        elif m!=0 and par=="i"and aposta=="p":
            din = din+x
        else:
            din=din-x
        print("Lucro de {0}".format(din))
       
        
                    
        
                    
    
    
          