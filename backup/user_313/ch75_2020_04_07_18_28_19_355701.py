def verifica_primos(l1):
    dicionario = {}
    for i in l1:
        if i == 0 or i == 1 or i == -1 :
            dicionario[i] = True
        elif i == 2 or i == 3 or i == 5 or i == 7:
            dicionario[i] = True
        elif i % 2 == 0:
            dicionario[i] = False
        elif i % 3 == 0:
            dicionario[i] = False
        elif i % 5 == 0:
            dicionario[i] = False
        elif i % 7 == 0:
            dicionario[i] = False
        else:
            dicionari[i] = True
           
          
    return dicionario