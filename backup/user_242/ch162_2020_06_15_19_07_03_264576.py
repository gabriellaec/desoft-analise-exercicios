lista = [1,3,7,9]
def verifica_lista(lista):
    par = True
    impar = True
    for i in lista:
        if i%2 == 0: 
            impar = False
        else:
            par = False
    if par and not impar:
        return 'par'
    elif impar and not par:
        return 'impar'
    return 'misturado'
        
    