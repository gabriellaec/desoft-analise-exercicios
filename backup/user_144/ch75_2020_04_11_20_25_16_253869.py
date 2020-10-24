    
def verifica_primos(lista):
    dic = {}
    for i in range(len(lista)):
        
        if  lista[i]>= 2:
            for y in range( 2, lista[i] ):
                if not ( lista[i] % y ):
                    dic[lista[y]] = False
                   
                else:
                    dic[lista[y]] = True
    return dic