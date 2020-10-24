def classifica_idade(i):
    i=int(i)
    if i<=11:
        a="crianca"
    elif i>11 and i<=17:
        a="adolecente"
    elif i>=18:
        a="adulto"
    return a