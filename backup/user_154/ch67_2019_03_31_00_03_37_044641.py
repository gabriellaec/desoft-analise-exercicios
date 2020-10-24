def alunos_impares(lista):
    result = []
    
    impar = False
    
    for x in lista:
        if impar:
            result.append(x)
            impar = False
        else:
            impar = True
    return result