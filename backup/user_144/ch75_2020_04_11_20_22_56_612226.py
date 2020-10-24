def verifica_primos(lista):
    dic = {}
    if x >= 2:
        for y in range( 2, x ):
            if not ( x % y ):
                dic[lista[y]] = False
               
            else:
                dic[lista[y]] = True
    return dic
    