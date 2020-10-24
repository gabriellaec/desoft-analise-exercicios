with open("texto.txt") as arquivo:
    conteudo = arquivo.read()
    caracteres = conteudo.split("")
    contagem = 0
    for x in caracteres:
        contagem += 1