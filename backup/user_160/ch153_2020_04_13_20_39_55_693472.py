def agrupa_por_idade(dicionario):
    dicionario2 = {}
    for i in range(len(dicionario)):
        if dicionario[0][i] <= 11:
            dicionario2[0][i] = dicionario[0][i]
            dicionario2[i][0] = 'criança'        
        if dicionario[0][i] <= 17:
            dicionario2[1][i] = dicionario[1][i]
            dicionario2[i][1] = 'adolescente'      
        if dicionario[0][i] <= 59:
            dicionario2[2][i] = dicionario[2][i]
            dicionario2[i][2] = 'adulto'  
        if dicionario[0][i] >= 60:
            dicionario2[3][i] = dicionario[3][i]
            dicionario2[i][3] = 'idoso'
print(dicionario2)                