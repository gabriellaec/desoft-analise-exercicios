with open('churras.txt', 'r') as arquivo:
    # Lista de string para cada linha
    linhas = arquivo.readlines()
    # Calcula custo
    custo = 0
    for compra in linhas:
        # Transforma lista[i] numa lista de strings
        lista = compra.split(',')
        qtde = int(lista[1])
        preco = float(lista[2])
        custo += qtde*preco