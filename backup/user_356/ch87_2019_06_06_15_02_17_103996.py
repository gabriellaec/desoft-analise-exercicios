def processa_linha(linha):
    saida = []
    colunas = linha.split(',')
    saida.append(colunas[0])
    saida.append(int(colunas[1]))
    saida.append(float(colunas[2]))
    return saida


with open('macacos-me-mordam.txt', 'r') as arquivo:
    linhas=arquivo.readlines()
    
saida=[]
for linha in linhas:
    saida.append(processa_linha(linha))
    for cada in saida:
        custo=cada[1]*cada[2]
print(custo)