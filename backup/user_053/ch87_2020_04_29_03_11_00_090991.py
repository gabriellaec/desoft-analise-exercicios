with open('churras.txt', 'r') as arquivo:
    # Lista de string para cada linha
    linhas_arquivo = arquivo.read()
    linhas = linhas_arquivo.split('\n')
    
# Calcula custo
custo = 0
for compra in linhas:
    # Transforma linhas[i] numa lista de strings
    listagem = compra.split(',')
    # Custo
    qtde = int(listagem[1])
    preco = float(listagem[2])
    custo += qtde*preco

print(custo)