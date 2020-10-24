def agrupa_por_idade(dicionario):
    dicionario2={}
    for i in dicionario:
         if dicionario[i]<=11:
             dicionario2[i]="criança"
         elif 12<=dicionario[i]<=17:
             dicionario2[i]="adolescente"
         elif 18<=dicionario[i]<=59:
             dicionario2[i]="adulto"
         else:
             dicionario2[i]="idoso"
    return dicionario2
