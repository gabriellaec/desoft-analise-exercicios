from random import randint


dinheiros = 100
    
while (dinheiros > 0):
        
    
    print (dinheiros)
    valor= int(input("Valor da sua aposta"))
    if valor != 0 :
        
        aposta=input("Se apostra um número digite n, se for Ímpar digite i e se for par digite p")
    

        if aposta == 'n':
            aposta=input("Digite um número de 1 a 36")
            d = (randint ( 0 , 36))
            if aposta == d:
                dinheiros += valor*35 
            else:
                dinheiros -=valor
            


        elif aposta == 'p':
            p_i= input( "Se escolherpar digite p, e se escolher ípar digite i")
            d = (randint ( 0 , 36))
            if p_i == 'p':
                if (d % 2 == 0) or (d == 0):
                    dinheiros += valor             
                else:
                    dinheiros -= valor 
            elif p_i == 'i':
                if d % 2 != 0:
                    dinheiros += valor
                else:
                    dinheiros -= valor
                
    else: 
        dinheiros -= dinheiros 