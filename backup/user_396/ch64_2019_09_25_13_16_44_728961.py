def nome_usuario(x):
    nome = ""
    i = 0
    while x[i] != '@':
        nome+=x[i]
        i += 1
    return nome

print(nome_usuario('usuario@insper.edu.br'))
    