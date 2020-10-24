def classifica_idade (i):
    if i <= 11:
        classi = "crianca"
    elif i >= 12 and i <= 17:
        classi = "adolescente"
    elif i >= 18:
        classi = "adulto"
        
    return classi