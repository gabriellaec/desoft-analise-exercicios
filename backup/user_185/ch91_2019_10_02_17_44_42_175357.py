with open('palavras.txt', 'r') as folder:
    dados = folder.read()
    splitado = dados.split()
    lista_iniciais_em_a = []
    numero_iniciais_em_a = 0
    i = 0
    while i < len(splitado):
        valor = splitado[i]
        inicial = valor[0]
        if inicial == 'a':
            lista_iniciais_em_a.append(inicial)
        i = i + 1
    numero_iniciais_em_a = len(lista_iniciais_em_a)