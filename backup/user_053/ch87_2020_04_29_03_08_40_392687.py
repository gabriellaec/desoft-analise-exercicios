with open('churras.txt', 'r') as arquivo:
    # Lista de string para cada linha
    linhas_arquivo = arquivo.read()
    linhas = linhas_arquivo.split('\n')
    
# Calcula custo
custo = 0
for compra in linhas:
    # Transforma linhas[i] numa lista de strings
    lista = compra.split(',')
    # Gasto
    qtde = int(lista[1])
    preco = float(lista[2])
    custo += qtde*preco