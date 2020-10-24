def verifica_primos (lista):
    dic = {}
    for n in lista:
        if n == -1 or n == 0 or n == 1:
            dic[n] = False
        elif n == 2 or n == 3:
            dic[n] = True
        else: 
            i = 3
            while n > i:
                if n%i == 0:
                    dic[n] = False
                    i += 1
                else:
                    dic[n] = True
                    i += 1
    return dic 
                
            
            
            
lista =[1, 10, 20 , 30, 0]
            