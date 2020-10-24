def verifica_progressao(lista):
    razaoA = [0] * (len(lista) - 1)
    razaoG = [0] * (len(lista) - 1)
    PA = True
    PG = True
    TestPG = True

    for e in range(0,len(lista)):                  #Se todos termos forem iguais 'AG'
        if lista[e] != lista[e-1]:
            break
        return "AG"


    for e in range(1,len(lista)):                  #É uma PA?
        razaoA[e - 1] = lista[e] - lista[e-1]
    for e in range(0, len(razaoA)):
        if razaoA[e] != razaoA[0]:
            PA = False

    for e in range(0,len(lista)):                   #Algum dos termos é igual a zero?
        if lista[e] == 0:                           #Se for não pode ser PG pois:                                                  #
            PG = False                              #Já foi testado se todos são iguais
            TestPG = False
            break

    
    if TestPG:                                      #É uma PG?
        for e in range(1,len(lista)):
            razaoG[e-1] = lista[e] / lista[e-1]
        for e in range(0, len(razaoG)):
            if razaoG[e] != razaoG[0]:
                PG = False


    if PA:
        return 'PA'
    elif PG:
        return 'PG'
    else:
        return 'NA'