import ramdom
a=true
while a:
    dinheiro=100
    numero=random.randint(1,36)
    aposta=input("valor da aposta")
    if aposta=0:
        a=False 
        print(dinheiro)
    elif aposta>dinheiro:
        aposta=format(input("valor da aposta"))
    else:
        pergunta2=str(input("vai apostar um n ou p/i"))
        if pergunta2=p:
            if p%2=numero%2:
                dinheiro+=aposta
                print(dinheiro)
            else:
                dinheiro-=aposta
                print(dinheiro)
        elif pergunta2=i:
            if i%2=numero%2:
                dinheiro+=aposta
                print(dinheiro)
            else:
                dinheiro-=aposta
                print(dinheiro)
        else:
            if pergunta2=numero:
                dinheiro+=35*aposta
                print(dinheiro)
            else:
                dinheiro-=aposta
                print(dinheiro)
             
            
                
            
    
    
        
                     
    