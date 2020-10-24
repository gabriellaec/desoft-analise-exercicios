def  classifica_idade(idade):
    if idade<=11:
        return 'crianca'
    if 11<idade<17:
        return 'adolescente'
    if idade>=17:
        return ' adulto'
c=classifica_idade(18)
print(c)