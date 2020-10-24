with open("texto.txt") as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split()
    contagem = 0
    for palavras in lista:
        contagem += 1
print(contagem)