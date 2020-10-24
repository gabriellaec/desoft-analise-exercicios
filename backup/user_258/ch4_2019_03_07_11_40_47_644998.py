
o= int(input('Qual a idade?'))
def classifica_idade (o):
    if o<= 11:
        return 'crianca'
    elif 12<=o<=17:
        return 'adolescente'
    else:
        return 'adulto'
print (classifica_idade (o))