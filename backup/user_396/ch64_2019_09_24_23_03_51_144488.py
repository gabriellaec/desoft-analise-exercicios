nome = []
def nome_usuario(x):
    i = 0
    while x[i] != '@':
        nome.append(x[i])
        i += 1
        return nome
    