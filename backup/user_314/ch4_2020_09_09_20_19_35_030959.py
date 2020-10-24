def classifica_idade(x):
    if (x<=11):
        res="crianca"
    elif (x>=12) and (x<=17):
        res="adolescente"
    else:
        res="adulto"
    return res