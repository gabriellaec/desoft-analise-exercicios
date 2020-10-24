def classifica_idade(x):
    if x<12:
        print('crianca')
    if 11<x<18:
        print('adolescente')
    if x>17:
        print('adulto')

print(classifica_idade(12))
