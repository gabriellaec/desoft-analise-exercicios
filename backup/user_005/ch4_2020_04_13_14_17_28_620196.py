import random
def classifica_idade(i):
    i = random.randint (0,99)
    if i <= 11:
        return ('crianca')
    elif i >= 12 and i <=17:
        return ('adolescente')
    else:
        return ('adulto')