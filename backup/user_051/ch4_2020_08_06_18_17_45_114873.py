def classifica_idade(i):
    i=int(i)
    if int(i)<=11:
        a="crianca"
    elif int(i)<=17:
        a="adolecente"
    elif int(i)>=18:
        a="adulto"
    return a