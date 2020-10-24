def classifica_idade(n):
    if n <=11:
        tipo = 'crianca'
    elif n >= 12 and n <= 17:
        tipo = 'adolescente'
    elif n >= 18:
        tipo = 'adulto'
        
    return tipo