def verifica_lista(lista):
    verifica_par = []
    verifica_impar = []
    if len(lista) == 0:
        return 'misturado'
    else:
        for i in lista:
            if i % 2 == 0:
                verifica_par.append(i)
            else:
                verifica_impar.append(i)
        if len(verifica_par) == len(lista):
            return 'par'
        elif len(verifica_impar) == len(lista):
            return 'ímpar'
        else:
            return 'misturado'