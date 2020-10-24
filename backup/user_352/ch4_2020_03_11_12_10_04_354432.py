def classifica_idade(i):
    if 0<=i<=11:
        resultado= "crianca"
    if 12<=i<=17:
        resultado= "adolescente"
    if i>=18:
        resultado= "adulto"
    return resultado