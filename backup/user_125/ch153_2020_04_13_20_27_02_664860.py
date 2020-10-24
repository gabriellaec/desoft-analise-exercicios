dicionario={'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}
def agrupa_por_idade(dici):
    dicionario_2={}
    for i in dicionario:
        if dici[i]<=11:
            dicionario2[i]="criança"
        elif 12<=dici[i]<=17:
            dicionario2[i]="adolescente"
        elif 18<=dici[i]<=59:
            dicionario_2[i]="adulto"
        else:
             dicionario_2[i]="idoso"
    return dicionario2  