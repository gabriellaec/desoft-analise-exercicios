def classifica_idade(i):
    if i<=11:
        a=str('crianca')
    elif i>11 and i<18:
        a=str('adolecente')
    elif i>=18:
        a=str('adulto')
    return a