def classifica_idade(i):
    b=int(i)
    if b<=11:
        a="crianca"
    elif b<=17:
        a="adolecente"
    elif b>=18:
        a="adulto"
    return a