def verifica_preco(titulo, cor, preco):
    for nome, cor in cor.items():
        if nome == titulo:
            return preco[cor]