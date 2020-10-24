def classifica_idade(i):
    if i<=11:
        return 'criança'
    if i>=12 or i<=17:
        return 'adolescente'
    if i>=18:
        return 'adulto'