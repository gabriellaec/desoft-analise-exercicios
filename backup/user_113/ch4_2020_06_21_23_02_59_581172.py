def classifica_idade(x):
    if 12<=x<=17:
        idade="adolescente" 
    elif x<=11:
        idade="crianca"
    elif x>=18:
        idade="adulto"
    return idade