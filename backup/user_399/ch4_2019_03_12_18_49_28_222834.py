def classifica_idade(a):
    a=int(input("qual a sua idade? "))
    if a<=11:
        c="crianca"
    elif 12<=a<=17:
        c="adolescente"
    else:
        c="adulto"
    return c