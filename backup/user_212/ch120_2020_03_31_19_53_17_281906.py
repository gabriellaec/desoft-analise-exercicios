from random import randint

def random.randint (dinheiros):
    dinheiros = 100
    
    while (dinheiros != 0):
        
    
        print (dinheiros)
        valor= int(input("Valor da sua aposta"))
            if valor = 0:
                return valor
        aposta=input("Se apostra um número digite n, se for Ímpar digite i e se for par digite p")
    
        d = (randint ( 1 , 36))

        if aposta= n:
            aposta=input("Digite um número de 1 a 36")
            if aposta= d:
                dinheiros += valor*35 
            else:
                dinheiros -=valor 


        elif aposta= p:
            if d % 2:
                dinheiros += valor             
            else:
                dinheiros -= valor 
        
        
        else:
            if d % 2:
                dinheiros -= valor
            else:
                dinheiros += valor
                
    return dinheiros 