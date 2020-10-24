def verifica_primos(lista):
    dici={}
    for n in lista:
        if n== 2:
            dici[n]=True 
        elif n==0 or n==1:
            dici[n]=False
        elif n%2 == 0:
            dici[n]= False 
        else:
            contador = 3
            while contador < n:
                if n%contador == 0: 
                    dici[n]= False 
                contador +=2
            dici[n]=True 
    return dici
            
        