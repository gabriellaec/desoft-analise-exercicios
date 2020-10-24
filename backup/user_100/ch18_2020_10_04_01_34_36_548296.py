def verifica_idade(i):
    if i<18:
        print('Não está liberado')
    else 18<i<21:
        print('Liberado Brasil')
    elif i>21:
        print('Liberado EUA e Brasil')