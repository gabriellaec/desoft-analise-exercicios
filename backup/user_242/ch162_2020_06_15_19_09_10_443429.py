def verifica_lista(valores):
    par = True
    impar = True
    for valor in valores:
        if valor%2 == 0: 
            impar = False
        else:
            par = False
    if par and not impar:
        return 'par'
    elif impar and not par:
        return 'impar'
    return 'misturado'
        
lista = [1,3,7,9]  
print(verifica_lista(lista))