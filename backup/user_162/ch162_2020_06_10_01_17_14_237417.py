def verifica_lista(lis):
    par = []
    impar = []
    for num in lis:
        if num % 2 == 0:
            par.append(num)
        else:
            impar.append(num)
    if len(par) != 0 and len(impar) == 0:
        return "par"
    elif len(par) == 0 and len(impar) != 0:
        return "ímpar" 
    else:
        return "misturado"
