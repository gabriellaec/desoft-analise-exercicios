def classifica_idade(a):
    if a<=0:
        return "idade inválida"
    else:
        if a<=11:
            c="crianca"
        elif 12 <= a <= 17:
            c="adolescente"
        else:
        	c="adulto"
        return c