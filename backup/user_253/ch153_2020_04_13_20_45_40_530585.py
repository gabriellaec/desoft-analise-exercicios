def agrupa_por_idade():
    pessoa=dict()
    pessoa['nome']= str(input('qual o nome?'))
    pessoa['idade']= int(input('qual a idade?'))
    if pessoa['idade'] <= 11:
        