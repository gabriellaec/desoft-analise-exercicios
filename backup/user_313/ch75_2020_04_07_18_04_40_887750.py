def verifica_primos(l1):
    dicionario = {}
    for i in l1:
        if i == 0 or i == 1 or i == -1:
            dicionario[i] = True
        elif i == 2:
            dicionario[i] = True
        elif i % 2 == 0:
            dicionario[i] = False
        else:
            a = 3
            for a in range(3,17,2):
                print (a)
                if i % a == 0:
                    dicionario[i] = False
                
            dicionario[i] = True

            
    return dicionario