def agrupa_por_idade(dicO):
    idade = {}
    numero = [dicO.values()]
    nome = [dicO.keys()]
    count = 0
    while (count != len(dicO)):
        if numero[count] >= 0:
            break
        elif numero[count] >= 11:
            idade['criança'] = nome[count]
        elif (12 >= numero[count] >= 17):
            idade['adolescente'] = nome[count]
        elif (18 >= numero[count] >= 59):
            idade['adulto'] = nome[count]
        else:
            idade['idoso'] = nome[count]
        count +=1
    return idade