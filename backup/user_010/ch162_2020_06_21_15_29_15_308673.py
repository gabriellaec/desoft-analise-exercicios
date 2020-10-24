def verifica_lista (lista):
    par=0
    impar=0
    for num in lista:
        if num==0:
            par+=1
        else:
            if num%2==0:
                par+=1
            else:
                impar+=1
    if len (lista)==0:
        return "misturado"
    if par==len(lista):
        return "par"
    elif impar==len(lista):
        return "ímpar"
    else:
        return "misturado"