def verifica_lista(lista):
    par = False
    impar = False
    for n in lista:
        if n%2 == 0: #se é par
            par = True
        else:
            impar = True
    if par == impar:
        return "misturado"
    elif par:
        return "par"
    else:
        return "ímpar"
        
    
            