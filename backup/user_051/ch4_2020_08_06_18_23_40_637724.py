def classifica_idade(i):
    i=int(i)
    if int(i)<=int(11):
        a="crianca"
    elif int(i)<=int(17):
        a="adolecente"
    elif int(i)>=int(18):
        a="adulto"
    return a