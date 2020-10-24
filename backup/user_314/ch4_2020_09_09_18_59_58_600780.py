def classifica_idade(x):
    if (x<=11):
        res="crianca"
    elif (x>11) and (x<18):
        res="adolescente"
    else:
        res="adulto"
    return res