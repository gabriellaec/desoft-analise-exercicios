def conta(nome):
    with open(nome, 'r') as arquivo:
        conteudo = arquivo.read()
        return len(conteudo)

print(conta('texto.txt'))