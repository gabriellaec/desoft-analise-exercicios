def verifica_lista (lista):
        if len(lista)==0:
            return("misturado")
            
        if all (e % 2== 0 for e in lista):
            return("par")
        if all (e % 2 != 0 for e in lista):
            return("ímpar")
            
        else:
            return("misturado")
                    
        