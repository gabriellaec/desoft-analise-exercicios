def verifica_lista (lista):
    i=0
    while i < len(lista):
        if len(lista)==0:
            return ("misturado")
        if lista[i] % 2 == 0:
            i+=1
            return ("par")
        if lista[i] % 2 != 0:
            return("impar")
        else:
            return("misturado")
        

                    
        