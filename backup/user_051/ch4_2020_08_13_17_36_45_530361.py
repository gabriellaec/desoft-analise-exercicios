def classifica_idade(i):
    if int(i)<=11:
        a="crianca"
    elif int(i)<=17:
        a="adolescente"
    elif int(i)>=18:
        a="adulto"
    return a
print (classifica_idade(12))