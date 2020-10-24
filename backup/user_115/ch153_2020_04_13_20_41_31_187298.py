def agrupa_por_idade(dicO):
    idade = {}
    numero = [dicO.values()]
    nome = [dicO.keys()]
    count = 0
    while (count != len(dicO)):
        for numero[count] in range (0, 12):
            idade['criança'] = nome[count]
        for numero[count] in range (12, 18):
            idade['adolescente'] = nome[count]
        for numero[count] in range (18, 60):
            idade['adulto'] = nome[count]
        for numero[count] in range (60, reverse = True):
            idade['idoso'] = nome[count]
        count +=1
    return idade