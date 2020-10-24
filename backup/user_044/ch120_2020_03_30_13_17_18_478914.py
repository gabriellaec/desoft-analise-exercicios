din = 100
while din>0:
    print('Disponível R${0}'.format(din))
    x = input("Quanto você irá apostar: ")
    aposta = input("Sua aposta é em um número ou paridade(n/p):  ")
    if aposta==n:
        num = input("Digite um número de 1 a 36: ")
    elif aposta==p:
        par = input("Escolha entre par ou ímpar(p/i): ")
    else:
        print("Apostas em apenas número e paridade!")
    sorteio = random.randint(1,36)
    m=sorteio%2
    if sorteio == num:
        ganhou= din + x*35
    elif m==0 and par==p:
        ganhou = din + x
    elif m!=0 and par==i:
    	ganhou = din+x
    else:    
		ganhou=din-x
        
        
        
                    
        
                    
    
    
          