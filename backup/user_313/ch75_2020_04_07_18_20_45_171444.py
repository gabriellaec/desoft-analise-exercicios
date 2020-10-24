def verifica_primos(l1):
    dicionario = {}
    for i in l1:
        if i == 0 or i == 1:
            dicionario[i] = True
        elif i == 2 or i == 3:
            dicionario[i] = True
        elif i % 2 == 0:
            dicionario[i] = False
        elif i == 9:
            dicionario[i] = False
    
        elif i > 3:
            a = 3
            while a < i:
                #print (a)
                if i % a == 0:
                    #print(a)
                    dicionario[i] = False
                    break
                else:
                    a = a + 2
            dicionario[i] = True

            
        

            
    return dicionario