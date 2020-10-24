
with open('criptografado.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    for i in conteudo:
        if i == 's':
            with open('criptografado.txt', 'w') as arquivo2:
                arquivo2.write(conteudo.replace(i, 'z'))
        if i == 'a':
            with open('criptografado.txt', 'w') as arquivo2:
                arquivo2.write(conteudo.replace(i, 'e'))
        if i == 'r':
            with open('criptografado.txt', 'w') as arquivo2:
                arquivo2.write(conteudo.replace(i, 'b'))
        if i == 'b':
            with open('criptografado.txt', 'w') as arquivo2:
                arquivo2.write(conteudo.replace(i, 'r'))
        if i == 'e':
            with open('criptografado.txt', 'w') as arquivo2:
                arquivo2.write(conteudo.replace(i, 'a'))
        if i == 'z':
            with open('criptografado.txt', 'w') as arquivo2:
                arquivo2.write(conteudo.replace(i, 's'))
    
