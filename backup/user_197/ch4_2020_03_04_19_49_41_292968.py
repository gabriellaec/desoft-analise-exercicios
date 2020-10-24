def calssifica_idade(a):
    a>=0
    if a<=11:
        return "crianca"

    elif a>=12 or a<=17:
        return "adolescente"

    else:
        return "adulto"