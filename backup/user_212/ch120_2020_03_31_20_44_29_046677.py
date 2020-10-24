from random import randint


dinheiros = 100
    
while (dinheiros > 0):
        
    
    print (dinheiros)
    valor= int(input("Valor da sua aposta"))
    if valor != 0 :
        
        aposta=input("Se aposta um número digite n, se for Ímpar digite i e se for par digite p")
    

        if aposta == 'n':
            aposta=int(input("Digite um número de 1 a 36"))
            d = (randint (0,36))
            if aposta == d:
                dinheiros += (valor*35)
                print (dinheiros)
            else:
                dinheiros -= valor
                print (dinheiros)
            


        elif aposta == 'p':
            p_i= input( "Se escolher par digite p, e se escolher ípar digite i")
           
            if p_i == 'p':
                d = (randint ( 0 , 36))
                if (d % 2 == 0) or (d == 0):
                    dinheiros += valor
                    print (dinheiros)
                else:
                    dinheiros -= valor
                    print (dinheiros)
            elif p_i == 'i':
                d = (randint ( 0 , 36))
                if d % 2 != 0 and d !=0:
                    dinheiros += valor
                    print (dinheiros)
                else:
                    dinheiros -= valor
                    print (dinheiros)
                
    else: 
        dinheiros -= dinheiros 
                